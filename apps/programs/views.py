from django.views.generic import ListView, DetailView
from .models import Program

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/list.html'
    context_object_name = 'programs'
    queryset = Program.objects.filter(is_public=True)

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programs/detail.html'
    queryset = Program.objects.filter(is_public=True)
