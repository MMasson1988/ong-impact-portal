from django.views.generic import TemplateView

from apps.accounts.mixins import StaffRequiredMixin
from apps.content.models import InternalNews, Photo
from apps.documents.models import Document
from apps.programs.models import Indicator, Program

from .models import DashboardWidget


class StaffHomeView(StaffRequiredMixin, TemplateView):
    """Accueil espace privé staff."""

    template_name = "dashboards/staff_home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["program_count"] = Program.objects.filter(is_published=True).count()
        ctx["indicator_count"] = Indicator.objects.count()
        ctx["document_count"] = Document.objects.filter(is_published=True).count()
        ctx["staff_news"] = InternalNews.objects.filter(is_published=True)[:5]
        ctx["widgets"] = DashboardWidget.objects.filter(is_active=True)
        return ctx


class StaffDashboardView(StaffRequiredMixin, TemplateView):
    template_name = "dashboards/staff_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["public_indicators"] = Indicator.objects.filter(is_public=True)[:10]
        ctx["private_documents"] = Document.objects.filter(is_published=True, is_private=True)[:10]
        ctx["recent_photos"] = Photo.objects.filter(is_published=True)[:12]
        ctx["widgets"] = DashboardWidget.objects.filter(is_active=True)
        return ctx
