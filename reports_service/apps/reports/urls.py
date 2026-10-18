from django.urls import path

from .views import (
    FoundReport,
    LostReport,
    MarkRecovered,
    ReportDetail,
    ReportListing,
    ReportUpdate,
)

urlpatterns = [
    path("reports/lost/", LostReport.as_view(), name="report-lost"),
    path("reports/found/", FoundReport.as_view(), name="report-found"),
    path("reports/", ReportListing.as_view(), name="report-list"),
    path("reports/<uuid:pk>/", ReportDetail.as_view(), name="report-detail"),
    path("reports/<uuid:pk>/update/", ReportUpdate.as_view(), name="report-update"),
    path("reports/<uuid:pk>/recover/", MarkRecovered.as_view(), name="report-recover"),
]
