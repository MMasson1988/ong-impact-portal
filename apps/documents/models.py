from django.db import models

from apps.programs.models import Program


def private_upload_path(instance, filename):
    return f"private/{instance.document_type}/{filename}"


def public_upload_path(instance, filename):
    return f"documents/{instance.document_type}/{filename}"


class Document(models.Model):
    """Document institutionnel ou rapport synthétique."""

    class DocType(models.TextChoices):
        INSTITUTIONAL = "institutional", "Institutionnel"
        REPORT = "report", "Rapport synthétique"
        POLICY = "policy", "Politique / procédure"
        OTHER = "other", "Autre"

    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=32, choices=DocType.choices, default=DocType.INSTITUTIONAL)
    summary = models.TextField(blank=True)
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    )
    file = models.FileField(upload_to=public_upload_path, blank=True, null=True)
    private_file = models.FileField(upload_to=private_upload_path, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_private = models.BooleanField("Fichier privé (staff)", default=False)
    published_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "document"

    def __str__(self):
        return self.title

    @property
    def storage_file(self):
        return self.private_file if self.is_private else self.file
