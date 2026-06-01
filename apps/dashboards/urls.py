from django.urls import path

from . import views

app_name = "dashboards"

urlpatterns = [
    path("", views.StaffHomeView.as_view(), name="staff_home"),
    path("vue-generale/", views.StaffDashboardView.as_view(), name="staff_dashboard"),
]
