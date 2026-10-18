from django.db import models
from django.contrib.auth.models import User
import uuid


class ItemStatus(models.TextChoices):
    RECOVERED = 'recovered'
    NOT_RECOVERED = 'not_recovered'

class ReportType(models.TextChoices):
    LOST = 'lost'
    FOUND = 'found'

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255, choices=ReportType.choices)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    item_image = models.ImageField(upload_to='reports/items/', blank=True, null=True)
    item_status = models.CharField(max_length=255, choices=ItemStatus.choices ,default=ItemStatus.NOT_RECOVERED)
    location = models.CharField(max_length=255)
    date_reported = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
