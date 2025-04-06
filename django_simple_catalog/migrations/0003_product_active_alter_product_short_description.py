# Generated by Django 5.2 on 2025-04-06 15:16

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_simple_catalog", "0002_sitesettings_category_description_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="short_description",
            field=models.CharField(
                help_text="Limited to 120 characters", max_length=120
            ),
        ),
    ]
