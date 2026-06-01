from django.urls import path

from . import views

app_name = "documents_private"

urlpatterns = [
    path("telecharger/<int:pk>/", views.PrivateFileDownloadView.as_view(), name="download"),
]
