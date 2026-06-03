from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('programmes/', include('apps.programs.urls')),
    path('statistiques/', include('apps.statistics.urls')),
    path('galerie/', include('apps.media_gallery.urls')),
    path('documents/', include('apps.documents.urls')),
    path('rapports/', include('apps.reports.urls')),
    path('actualites/', include('apps.news.urls')),
    path('staff/', include('apps.dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
