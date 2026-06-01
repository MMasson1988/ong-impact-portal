from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


GROUPS = {
    "SuperAdmin": "Tous les droits de gestion",
    "Communicator": "Actualités, médias, pages institutionnelles",
    "ProgramManager": "Programmes, indicateurs, rapports",
    "Staff": "Lecture espace privé",
}


class Command(BaseCommand):
    help = "Crée les groupes de rôles ONG Impact Portal."

    def handle(self, *args, **options):
        for name in GROUPS:
            group, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Groupe créé : {name}"))
            else:
                self.stdout.write(f"Groupe existant : {name}")

        superadmin = Group.objects.get(name="SuperAdmin")
        all_perms = Permission.objects.all()
        superadmin.permissions.set(all_perms)
        self.stdout.write(self.style.SUCCESS("Permissions assignées à SuperAdmin."))
