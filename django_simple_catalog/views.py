"""Views."""

# Standard Library
import logging
from datetime import timedelta

# Django
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Category, Product  # Adjust import paths as needed

logger = logging.getLogger(__name__)


def index(request):
    """
    Main view for the catalog.

    This view shows two lists of products on the same page:

    1. Products created in the last 30 days
    2. Products with a sale price

    Each list is paginated with 6 items per page.

    The view also logs the count of new and sale products to the logger.

    :param request: The request object
    :return: A rendered HTML page with the two lists of products
    """
    now = timezone.now()

    # Products created in the last 30 days
    new_products_qs = Product.objects.filter(
        created_at__gte=now - timedelta(days=30), active=True
    ).order_by("-created_at")

    # Products with a sale price
    sale_products_qs = Product.objects.filter(
        sale_price__isnull=False, active=True
    ).order_by("-created_at")

    # Paginate both lists (6 items per page)
    new_paginator = Paginator(new_products_qs, 6)
    sale_paginator = Paginator(sale_products_qs, 6)

    new_page = request.GET.get("new_page")
    sale_page = request.GET.get("sale_page")

    new_products = new_paginator.get_page(new_page)
    sale_products = sale_paginator.get_page(sale_page)
    context = {
        "new_products": new_products,
        "sale_products": sale_products,
    }
    return render(request, "django_simple_catalog/index.html", context)


def category_detail(request, slug):
    """
    Detail view for a category.

    This view renders a page for a given category by its slug,
    showing the category name, description, and a list of products
    associated with the category.

    :param request: The request object
    :param slug: The slug of the category
    :return: A rendered HTML page with the category information
    """
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(
        category=category, active=True
    )  # Filter active products
    return render(
        request,
        "django_simple_catalog/category.html",
        {"category": category, "products": products},
    )


def ajax_search_products(request):
    """
    AJAX view to search products by name.

    The view takes a query parameter "q" and returns a JSON response
    with a list of 5 products that match the query, sorted by creation date.

    Each product is represented as a dictionary with two keys: "name" and "price".

    :param request: The request object
    :return: A JSON response with the search results
    """
    query = request.GET.get("q", "")
    results = []

    if query:
        products = Product.objects.filter(Q(name__icontains=query)).order_by(
            "-created_at"
        )[:5]
        for p in products:
            results.append(
                {
                    "name": p.name,
                    "price": str(p.price),
                }
            )

    return JsonResponse({"results": results})
