from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'super_admin', _('Super Administrateur')
        MANAGER     = 'manager',     _('Manager ONG')
        STAFF       = 'staff',       _('Staff Terrain')
        PARTNER     = 'partner',     _('Partenaire')
        PUBLIC      = 'public',      _('Visiteur')
    role     = models.CharField(max_length=20, choices=Role.choices, default=Role.PUBLIC)
    phone    = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=100, blank=True)
    avatar   = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio      = models.TextField(blank=True)
    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')
    def is_staff_member(self) -> bool:
        return self.role in [self.Role.SUPER_ADMIN, self.Role.MANAGER, self.Role.STAFF]
