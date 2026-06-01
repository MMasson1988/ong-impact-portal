from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .mixins import StaffRequiredMixin


class StaffLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboards:staff_home")


class StaffLogoutView(LogoutView):
    next_page = reverse_lazy("core:home")


class ProfileView(StaffRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["profile_user"] = self.request.user
        return ctx
