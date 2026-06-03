from django.urls import path
from django.views.generic import ListView
from .models import Album

app_name = 'media_gallery'
urlpatterns = [path('', ListView.as_view(model=Album, template_name='gallery/list.html',
    queryset=Album.objects.filter(is_public=True), context_object_name='albums'), name='list')]
