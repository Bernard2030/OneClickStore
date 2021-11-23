# Generated by Django 3.2.9 on 2021-11-22 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_smsmessage"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailMessage",
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
                ("email", models.EmailField(blank=True, max_length=254)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("message", models.TextField(blank=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email_messages",
                        to="products.userprofile",
                    ),
                ),
            ],
        ),
    ]
