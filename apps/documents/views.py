from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from apps.accounts.mixins import StaffRequiredMixin

from .models import Document


class DocumentListView(ListView):
    model = Document
    template_name = "documents/document_list.html"
    context_object_name = "documents"
    paginate_by = 15

    def get_queryset(self):
        return Document.objects.filter(is_published=True, is_private=False)


class DocumentDetailView(DetailView):
    model = Document
    template_name = "documents/document_detail.html"
    context_object_name = "document"

    def get_queryset(self):
        return Document.objects.filter(is_published=True, is_private=False)


class StaffDocumentListView(StaffRequiredMixin, ListView):
    model = Document
    template_name = "documents/staff_document_list.html"
    context_object_name = "documents"
    paginate_by = 20

    def get_queryset(self):
        return Document.objects.filter(is_published=True)


class PrivateFileDownloadView(StaffRequiredMixin, DetailView):
    """Sert les fichiers privés après contrôle d'accès — jamais en URL directe."""

    model = Document

    def get(self, request, *args, **kwargs):
        document = get_object_or_404(
            Document,
            pk=kwargs["pk"],
            is_published=True,
            is_private=True,
        )
        f = document.private_file
        if not f:
            raise Http404("Fichier introuvable.")
        return FileResponse(f.open("rb"), as_attachment=True, filename=f.name.split("/")[-1])
