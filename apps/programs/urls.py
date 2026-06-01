from django.urls import path

from . import views

app_name = "programs"

urlpatterns = [
    path("", views.ProgramListView.as_view(), name="list"),
    path("indicateurs/", views.IndicatorListView.as_view(), name="indicators"),
    path("<slug:slug>/", views.ProgramDetailView.as_view(), name="detail"),
]
