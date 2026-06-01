from django.urls import path

from . import views

app_name = "documents"

urlpatterns = [
    path("", views.DocumentListView.as_view(), name="list"),
    path("staff/", views.StaffDocumentListView.as_view(), name="staff_list"),
    path("<int:pk>/", views.DocumentDetailView.as_view(), name="detail"),
]
