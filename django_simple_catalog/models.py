"""Models."""

# Standard Library
import uuid

# Django
from django.core.files.storage import default_storage
from django.db import models
from django.urls import reverse  # To generate URLs dynamically
from django.utils.text import slugify


class SiteSettings(models.Model):
    """Site settings model."""

    site_name = models.CharField(max_length=255)
    home_page_description = models.TextField()

    class Meta:
        """Meta class."""

        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        """Return the site name."""
        return self.site_name

    @classmethod
    def get_instance(cls):
        """Returns the single instance of SiteSettings, creating one if it doesn't exist."""
        instance = cls.objects.get_or_create(
            pk=1
        )  # You can store the single instance with a constant PK
        return instance


class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=100, blank=False, null=False)  # Required field
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcategories",
    )
    description = models.TextField(blank=True, null=True)  # Optional field
    order = models.IntegerField(
        default=100, blank=False, null=False
    )  # New field for ordering

    class Meta:
        """Meta class."""

        verbose_name_plural = "Categories"

    def __str__(self):
        """Return the category name."""
        return self.name

    def save(self, *args, **kwargs):
        """Save the category and generate the slug if not set."""
        # Automatically generate the slug from the name if not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return the absolute URL for the category detail page."""
        return reverse(
            "category_detail", kwargs={"slug": self.slug}
        )  # Assuming you have a detail page for categories

    # Method to check if the category has subcategories
    def has_subcategories(self):
        """Check if the category has subcategories."""
        return self.subcategories.exists()


def product_image_upload_to(filename):
    """Generate a unique path for the uploaded image."""
    # Generate a unique UUID for the file
    unique_id = uuid.uuid4().hex  # Generates a unique identifier
    # Split the file extension from the filename
    extension = filename.split(".")[-1]
    # Return a path with the unique ID and original file extension
    return f"products/{unique_id}.{extension}"


class Product(models.Model):
    """Product model."""

    name = models.CharField(max_length=200, blank=False, null=False)  # Required field
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        blank=False,
        null=False,
    )  # Required field
    image = models.ImageField(
        upload_to=product_image_upload_to, null=True, blank=True
    )  # Updated image field
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=False, null=False
    )  # Required field
    sale_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    short_description = models.CharField(
        max_length=120, help_text="Limited to 120 characters", null=True, blank=True
    )
    long_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)  # New active toggle field

    def __str__(self):
        """Return the product name."""
        return self.name

    def get_current_price(self):
        """
        Return the current price of the product.

        If the product has a sale price, returns the sale price.
        Otherwise, returns the original price.

        Returns:
            Decimal: The current price of the product.
        """
        return (
            self.sale_price if self.sale_price else self.price
        )  # Return sale price if available, else original price

    def delete(self, *args, **kwargs):
        # Delete the image file if it exists
        """
        Delete the product instance and the associated image file if it exists.

        This custom delete method is used to delete the image file associated with
        the product instance. It first checks if the image field is set and if the
        file exists in the default storage. If both conditions are true, it deletes
        the image file using the default storage backend. Finally, it calls the
        original delete method to delete the model instance.
        """
        if self.image:
            # Use the default storage backend to delete the image file
            if default_storage.exists(self.image.name):
                default_storage.delete(self.image.name)
        # Call the original delete method to delete the model instance
        super().delete(*args, **kwargs)
