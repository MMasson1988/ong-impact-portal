from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView

from apps.content.models import InternalNews, Photo
from apps.programs.models import Indicator, Program

from .models import InstitutionalPage


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_programs"] = Program.objects.filter(
            is_published=True, is_featured=True
        )[:3]
        ctx["latest_news"] = InternalNews.objects.filter(is_published=True)[:5]
        ctx["recent_photos"] = Photo.objects.filter(is_published=True)[:8]
        ctx["key_indicators"] = Indicator.objects.filter(
            is_public=True, is_featured=True
        )[:6]
        return ctx


class AboutView(TemplateView):
    template_name = "core/about.html"


class InstitutionalPageView(DetailView):
    model = InstitutionalPage
    template_name = "core/institutional_page.html"
    context_object_name = "page"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)
