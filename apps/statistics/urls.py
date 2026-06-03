from django.urls import path
from django.views.generic import TemplateView

app_name = 'statistics'
urlpatterns = [path('', TemplateView.as_view(template_name='statistics/index.html'), name='index')]
