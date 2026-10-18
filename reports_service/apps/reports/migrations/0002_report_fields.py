import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(name="Report"),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "report_type",
                    models.CharField(
                        choices=[("lost", "Lost"), ("found", "Found")],
                        max_length=255,
                    ),
                ),
                ("item_name", models.CharField(max_length=255)),
                ("item_description", models.TextField(blank=True, null=True)),
                (
                    "item_image",
                    models.ImageField(blank=True, null=True, upload_to="reports/items/"),
                ),
                (
                    "item_status",
                    models.CharField(
                        choices=[
                            ("recovered", "Recovered"),
                            ("not_recovered", "Not Recovered"),
                        ],
                        default="not_recovered",
                        max_length=255,
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                ("date_reported", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
