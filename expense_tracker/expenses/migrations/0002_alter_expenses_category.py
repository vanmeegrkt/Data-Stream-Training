# Generated by Django 5.2.1 on 2025-05-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenses",
            name="category",
            field=models.CharField(
                choices=[
                    ("Personal", "Personal"),
                    ("Friends", "Friends"),
                    ("Family", "Family"),
                ],
                max_length=20,
            ),
        ),
    ]
