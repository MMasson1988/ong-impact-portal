from django.urls import path

from . import views

app_name = "content"

urlpatterns = [
    path("actualites/", views.NewsListView.as_view(), name="news_list"),
    path("actualites/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("realisations/", views.AchievementListView.as_view(), name="achievements"),
    path("galerie/", views.PhotoGalleryView.as_view(), name="gallery"),
]
