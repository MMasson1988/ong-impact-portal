from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("comptes/", include("apps.accounts.urls")),
    path("programmes/", include("apps.programs.urls")),
    path("contenus/", include("apps.content.urls")),
    path("documents/", include("apps.documents.urls")),
    path("tableaux-de-bord/", include("apps.dashboards.urls")),
    path("fichiers-prives/", include("apps.documents.urls_private")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
