"""Context processors."""

from .models import Category, SiteSettings


def navbar_menu(request):  # pylint: disable=unused-argument
    """
    Adds a list of top-level categories and their subcategories to the context
    for use in the navbar.
    """
    # Get top-level categories (no parent)
    top_level_categories = Category.objects.filter(parent__isnull=True).order_by(
        "order"
    )

    # Create a list of categories with their subcategories
    menu_items = []
    for category in top_level_categories:
        subcategories = category.subcategories.all().order_by("order")
        menu_items.append(
            {
                "name": category.name,
                "url": category.get_absolute_url(),
                "subcategories": subcategories,
            }
        )

    return {"menu_items": menu_items}


def site_settings(request):  # pylint: disable=unused-argument
    """
    Adds the site settings to the context. This is used by the base template
    to display the site name and description.
    """

    return {"site_settings": SiteSettings.objects.first()}
