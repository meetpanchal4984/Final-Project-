# Generated by Django 5.0.4 on 2024-04-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("Fristname", models.CharField(max_length=50)),
                ("Lastname", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=50)),
                ("Contact", models.CharField(max_length=50)),
                ("Password", models.CharField(max_length=50)),
            ],
        ),
    ]
