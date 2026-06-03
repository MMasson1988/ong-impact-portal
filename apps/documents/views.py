from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import Document

ACCESS_RULES = {
    'public':       lambda user: True,
    'partner':      lambda user: user.is_authenticated and user.role in ['partner','staff','manager','super_admin'],
    'staff':        lambda user: user.is_authenticated and user.is_staff_member(),
    'confidential': lambda user: user.is_authenticated and user.role in ['manager','super_admin'],
}

@login_required
def serve_document(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    check = ACCESS_RULES.get(doc.access_level, lambda u: False)
    if not check(request.user): raise PermissionDenied('Acces non autorise.')
    doc.download_count += 1
    doc.save(update_fields=['download_count'])
    return FileResponse(doc.file.open('rb'), as_attachment=True,
                        filename=doc.file.name.split('/')[-1])
