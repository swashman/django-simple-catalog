# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# Django Simple Catalog
from django_simple_catalog import __version__


class ExampleConfig(AppConfig):
    name = "django_simple_catalog"
    label = "django_simple_catalog"
    verbose_name = _(f"Django Simple Catalog v{__version__}")
