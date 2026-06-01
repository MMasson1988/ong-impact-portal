from django.views.generic import DetailView, ListView

from apps.accounts.mixins import StaffRequiredMixin

from .models import Achievement, InternalNews, Photo


def _staff_or_public_filter(user, queryset):
    if user.is_authenticated and (
        user.is_superuser
        or user.groups.filter(name__in=["SuperAdmin", "Communicator", "ProgramManager", "Staff"]).exists()
    ):
        return queryset.filter(is_published=True)
    return queryset.filter(is_published=True, is_staff_only=False)


class NewsListView(ListView):
    model = InternalNews
    template_name = "content/news_list.html"
    context_object_name = "news_list"
    paginate_by = 10

    def get_queryset(self):
        return _staff_or_public_filter(self.request.user, InternalNews.objects.all())


class NewsDetailView(DetailView):
    model = InternalNews
    template_name = "content/news_detail.html"
    context_object_name = "article"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return _staff_or_public_filter(self.request.user, InternalNews.objects.all())


class AchievementListView(ListView):
    model = Achievement
    template_name = "content/achievement_list.html"
    context_object_name = "achievements"
    paginate_by = 12

    def get_queryset(self):
        return _staff_or_public_filter(self.request.user, Achievement.objects.all())


class PhotoGalleryView(ListView):
    model = Photo
    template_name = "content/photo_gallery.html"
    context_object_name = "photos"
    paginate_by = 24

    def get_queryset(self):
        return _staff_or_public_filter(self.request.user, Photo.objects.select_related("program"))


class StaffNewsListView(StaffRequiredMixin, ListView):
    model = InternalNews
    template_name = "content/staff_news_list.html"
    context_object_name = "news_list"
    paginate_by = 15

    def get_queryset(self):
        return InternalNews.objects.filter(is_published=True)
