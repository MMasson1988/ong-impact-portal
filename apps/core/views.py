from django.views.generic import TemplateView
from apps.statistics.models import KeyStat
from apps.programs.models import Program
from apps.news.models import NewsArticle

class HomeView(TemplateView):
    template_name = 'core/home.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['key_stats']   = KeyStat.objects.filter(is_active=True)
        ctx['programs']    = Program.objects.filter(is_public=True, is_featured=True)[:3]
        ctx['recent_news'] = NewsArticle.objects.filter(is_published=True, audience='public')[:4]
        return ctx
