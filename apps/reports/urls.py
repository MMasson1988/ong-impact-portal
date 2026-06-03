from django.urls import path
from django.views.generic import ListView
from .models import Report

app_name = 'reports'
urlpatterns = [path('', ListView.as_view(model=Report, template_name='reports/list.html',
    queryset=Report.objects.filter(is_public=True), context_object_name='reports'), name='list')]
