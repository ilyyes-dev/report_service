from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "title",
            "report_type",
            "item_name",
            "item_description",
            "item_image",
            "item_status",
            "location",
            "date_reported",
            "created_at",
            "updated_at",
            "owner",
        )
        read_only_fields = (
            "id",
            "report_type",
            "item_status",
            "owner",
            "created_at",
            "updated_at",
        )
