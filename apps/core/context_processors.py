from .models import SiteSettings


def site_context(request):
    settings = SiteSettings.load()
    return {
        "site_settings": settings,
        "site_name": settings.site_name,
    }
