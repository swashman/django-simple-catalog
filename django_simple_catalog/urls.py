"""Routes."""

# Django
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("ajax/search/", views.ajax_search_products, name="ajax_search"),
]
