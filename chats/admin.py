from django.contrib import admin
from .models import Dataset, AnalysisHistory


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "filename",
        "user",
        "rows",
        "columns",
        "uploaded_at",
    )

    list_filter = ("uploaded_at", "user")
    search_fields = ("name", "filename", "user__username")


@admin.register(AnalysisHistory)
class AnalysisHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "dataset_name",
        "user",
        "chart_type",
        "created_at",
    )

    list_filter = ("chart_type", "created_at", "user")
    search_fields = (
        "question",
        "dataset_name",
        "user__username",
    )