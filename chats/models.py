from django.db import models
from django.contrib.auth.models import User


class Dataset(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="datasets"
    )
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    rows = models.IntegerField(default=0)
    columns = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AnalysisHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="analysis_history"
    )
    dataset_name = models.CharField(max_length=255)
    question = models.TextField()
    sql_query = models.TextField(blank=True, null=True)
    chart_type = models.CharField(max_length=50, blank=True, null=True)
    insight = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]