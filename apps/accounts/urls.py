from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("connexion/", views.StaffLoginView.as_view(), name="login"),
    path("deconnexion/", views.StaffLogoutView.as_view(), name="logout"),
    path("profil/", views.ProfileView.as_view(), name="profile"),
]
