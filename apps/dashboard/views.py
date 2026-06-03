from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from apps.statistics.models import Indicator, KeyStat
from apps.programs.models import Program
from apps.news.models import NewsArticle
from apps.documents.models import Document

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self): return self.request.user.is_staff_member()

class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self): return self.request.user.role in ['manager','super_admin']

class DashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['programs']    = Program.objects.filter(status='active')
        ctx['indicators']  = Indicator.objects.select_related('program').all()
        ctx['key_stats']   = KeyStat.objects.filter(is_active=True).order_by('order')
        ctx['recent_news'] = NewsArticle.objects.filter(is_published=True)[:5]
        ctx['documents']   = Document.objects.filter(access_level__in=['staff','public'])[:10]
        return ctx
