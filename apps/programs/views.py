from django.views.generic import DetailView, ListView

from .models import Indicator, Program


class ProgramListView(ListView):
    model = Program
    template_name = "programs/program_list.html"
    context_object_name = "programs"
    paginate_by = 12

    def get_queryset(self):
        return Program.objects.filter(is_published=True)


class ProgramDetailView(DetailView):
    model = Program
    template_name = "programs/program_detail.html"
    context_object_name = "program"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Program.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["indicators"] = self.object.indicators.filter(is_public=True)
        return ctx


class IndicatorListView(ListView):
    model = Indicator
    template_name = "programs/indicator_list.html"
    context_object_name = "indicators"
    paginate_by = 20

    def get_queryset(self):
        return Indicator.objects.filter(is_public=True).select_related("program")
