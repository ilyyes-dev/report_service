from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ItemStatus, Report, ReportType
from .serializers import ReportSerializer

#ramzyy l3zizz

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner_id == request.user.id


class LostReport(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, report_type=ReportType.LOST)


class FoundReport(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, report_type=ReportType.FOUND)


class ReportListing(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        q = Report.objects.select_related("owner")
        search = self.request.query_params.get("search")
        if search is not None:
            q = q.filter(
                Q(item_name__icontains=search) | Q(item_description__icontains=search)
            )

        report_type = self.request.query_params.get("report_type")
        if report_type is not None:
            q = q.filter(report_type=report_type)

        item_status = self.request.query_params.get("item_status")
        if item_status is not None:
            q = q.filter(item_status=item_status)

        location = self.request.query_params.get("location")
        if location is not None:
            q = q.filter(location__icontains=location)

        date_reported = self.request.query_params.get("date_reported")
        if date_reported is not None:
            q = q.filter(date_reported=date_reported)
        return q


class ReportDetail(generics.RetrieveAPIView):
    queryset = Report.objects.select_related("owner")
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]


class ReportUpdate(generics.UpdateAPIView):
    queryset = Report.objects.select_related("owner")
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class MarkRecovered(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def post(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        self.check_object_permissions(request, report)
        if report.item_status == ItemStatus.RECOVERED:
            return Response(
                {"information": "This item is already recovered."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        report.item_status = ItemStatus.RECOVERED
        report.save(update_fields=["item_status", "updated_at"])
        return Response(ReportSerializer(report).data, status=status.HTTP_200_OK)
