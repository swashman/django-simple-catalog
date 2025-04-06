"""Admin site."""

# Django
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe

from .models import Category, Product, SiteSettings


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_parent(self):
        parent = self.cleaned_data.get("parent")
        if parent and parent.parent:
            raise ValidationError(
                "You cannot select a category that already has a parent as a parent."
            )
        return parent


# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = (
        "name",
        "parent",
        "order",
    )  # Only display 'name' and 'parent' in the list
    search_fields = ("name",)  # Search by name

    # Exclude 'slug' field from the form in the admin
    exclude = ("slug",)


# Custom form for Product Admin to modify the category field behavior
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    # Override the category field to show categories based on whether they have subcategories
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # Start with all categories
        widget=forms.Select,
        label="Category",
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get categories that do not have subcategories (parent is null AND no subcategories)
        categories_without_subcategories = Category.objects.filter(
            parent__isnull=True
        ).filter(
            subcategories__isnull=True  # Exclude categories that have subcategories
        )

        # Get all subcategories (categories with a parent)
        categories_with_subcategories = Category.objects.filter(parent__isnull=False)

        # Combine both sets: categories without subcategories and subcategories themselves
        queryset = categories_without_subcategories | categories_with_subcategories

        # Update the category field's queryset to reflect the filtered categories
        self.fields["category"].queryset = queryset

        # Update the category dropdown to show "Category > Subcategory" format
        self.fields["category"].widget.choices = [
            (
                category.id,
                (
                    f"{category.parent.name} > {category.name}"
                    if category.parent
                    else category.name
                ),
            )
            for category in self.fields["category"].queryset
        ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        "name",
        "category",
        "active",
        "price",
        "sale_price",
        "created_at",
        "image_tag",
    )
    list_filter = (
        "active",
        "category",
    )
    search_fields = ("name", "category__name")
    ordering = ("-created_at",)
    fields = (
        "name",
        "category",
        "active",
        "price",
        "sale_price",
        "short_description",
        "long_description",
        "image",
        "created_at",
    )
    readonly_fields = ("created_at", "image_tag")  # Make image_tag readonly in admin

    # Method to display the image in the admin list view
    @admin.display(description="Image")
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"

    # Allow image upload functionality
    def save_model(self, request, obj, form, change):
        obj.save()


# SiteSettings Admin
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name",)
    search_fields = ("site_name",)

    def save_model(self, request, obj, form, change):
        # Ensure only one instance of SiteSettings exists
        if not SiteSettings.objects.exists() or change:
            obj.save()
