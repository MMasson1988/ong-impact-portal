from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("a-propos/", views.AboutView.as_view(), name="about"),
    path("pages/<slug:slug>/", views.InstitutionalPageView.as_view(), name="institutional_page"),
]
