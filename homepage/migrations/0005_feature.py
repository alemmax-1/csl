# Generated by Django 5.2 on 2025-04-18 07:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0004_alter_marketing_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        default="placeholder", max_length=255, verbose_name="image"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("order", models.IntegerField(default=0, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
