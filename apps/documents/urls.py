from django.urls import path
from . import views

app_name = 'documents'
urlpatterns = [path('<int:pk>/download/', views.serve_document, name='download')]
