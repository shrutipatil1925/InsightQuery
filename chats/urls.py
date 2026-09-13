from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name="chat"),
    path("database/", views.datasets, name="database"),
    path("history/", views.history, name="history"),
]