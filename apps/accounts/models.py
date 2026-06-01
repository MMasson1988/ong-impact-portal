from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Utilisateur staff avec profil institutionnel."""

    class Role(models.TextChoices):
        SUPER_ADMIN = "super_admin", "Super administrateur"
        COMMUNICATOR = "communicator", "Communication"
        PROGRAM_MANAGER = "program_manager", "Responsable programme"
        STAFF = "staff", "Personnel"

    role = models.CharField(
        max_length=32,
        choices=Role.choices,
        default=Role.STAFF,
    )
    job_title = models.CharField("Fonction", max_length=120, blank=True)
    department = models.CharField("Service", max_length=120, blank=True)
    phone = models.CharField("Téléphone", max_length=30, blank=True)
    avatar = models.ImageField("Photo", upload_to="avatars/", blank=True, null=True)

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def is_staff_member(self):
        return self.is_active and (
            self.is_superuser
            or self.groups.filter(
                name__in=[
                    "SuperAdmin",
                    "Communicator",
                    "ProgramManager",
                    "Staff",
                ]
            ).exists()
        )
