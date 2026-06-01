"""
Charge des données de démonstration pour ONG Impact Portal.
Idempotent : relançable sans doublons (get_or_create sur slugs).
"""
from datetime import date, timedelta
from io import BytesIO

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.content.models import Achievement, InternalNews, Photo
from apps.core.models import InstitutionalPage, SiteSettings
from apps.dashboards.models import DashboardWidget
from apps.documents.models import Document
from apps.programs.models import Indicator, Program

User = get_user_model()

DEMO_STAFF_USERNAME = "demo.staff"
DEMO_STAFF_PASSWORD = "DemoONG2026!"


def _placeholder_file(filename: str):
    from django.core.files.base import ContentFile
    from PIL import Image

    buf = BytesIO()
    Image.new("RGB", (640, 400), color=(13, 107, 92)).save(buf, format="PNG")
    return ContentFile(buf.getvalue(), name=filename)


class Command(BaseCommand):
    help = "Charge programmes, indicateurs, actualités, documents et compte staff de démo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--with-staff-user",
            action="store_true",
            help="Crée l'utilisateur demo.staff (mot de passe affiché en fin de commande).",
        )

    def handle(self, *args, **options):
        self._site_settings()
        self._institutional_pages()
        programs = self._programs()
        self._indicators(programs)
        self._news(programs)
        self._achievements(programs)
        self._photos(programs)
        self._documents(programs)
        self._dashboard_widgets()
        if options["with_staff_user"]:
            self._demo_staff_user()
        self.stdout.write(self.style.SUCCESS("Données de démonstration chargées."))

    def _site_settings(self):
        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                "site_name": "ONG Impact Portal",
                "tagline": "Centraliser l'impact, partager la connaissance institutionnelle",
                "mission": (
                    "Notre ONG accompagne les communautés vulnérables par des programmes "
                    "d'éducation, de santé et de résilience climatique."
                ),
                "contact_email": "contact@ong-impact-portal.org",
                "contact_phone": "+225 00 00 00 00",
                "address": "Abidjan, Côte d'Ivoire",
            },
        )

    def _institutional_pages(self):
        pages = [
            {
                "slug": "gouvernance",
                "title": "Gouvernance",
                "summary": "Organisation et principes de gouvernance.",
                "body": "Conseil d'administration, assemblée générale, charte éthique.",
                "order": 1,
            },
            {
                "slug": "partenariats",
                "title": "Partenariats",
                "summary": "Bailleurs et partenaires techniques.",
                "body": "Coopération avec institutions publiques, ONG locales et bailleurs internationaux.",
                "order": 2,
            },
        ]
        for data in pages:
            InstitutionalPage.objects.update_or_create(slug=data["slug"], defaults=data)

    def _programs(self):
        specs = [
            {
                "slug": "education-rurale",
                "name": "Éducation rurale",
                "summary": "Scolarisation et kits pédagogiques en zones rurales.",
                "description": "Construction de salles de classe, formation des enseignants, fournitures.",
                "sector": "Éducation",
                "region": "Nord",
                "is_featured": True,
                "order": 1,
            },
            {
                "slug": "sante-communautaire",
                "name": "Santé communautaire",
                "summary": "Accès aux soins primaires et sensibilisation.",
                "description": "Cliniques mobiles, vaccination, nutrition infantile.",
                "sector": "Santé",
                "region": "Centre",
                "is_featured": True,
                "order": 2,
            },
            {
                "slug": "resilience-climat",
                "name": "Résilience climatique",
                "summary": "Adaptation agricole et gestion des ressources en eau.",
                "description": "Puits, irrigation durable, formations agroécologiques.",
                "sector": "Environnement",
                "region": "Est",
                "is_featured": False,
                "order": 3,
            },
        ]
        programs = []
        today = date.today()
        for spec in specs:
            program, _ = Program.objects.update_or_create(
                slug=spec["slug"],
                defaults={
                    **spec,
                    "start_date": today - timedelta(days=400),
                    "is_published": True,
                },
            )
            if not program.cover_image:
                program.cover_image.save(
                    f"cover-{spec['slug']}.png",
                    _placeholder_file(f"cover-{spec['slug']}.png"),
                    save=True,
                )
            programs.append(program)
        return programs

    def _indicators(self, programs):
        edu, sante, climat = programs
        rows = [
            (edu, "Élèves scolarisés", "12 450", "élèves", "2025", True, True),
            (edu, "Salles construites", "28", "salles", "2025", True, False),
            (sante, "Consultations", "34 200", "consultations", "2025", True, True),
            (sante, "Enfants vaccinés", "8 900", "enfants", "2025", True, False),
            (climat, "Hectares restaurés", "1 250", "ha", "2025", True, True),
            (None, "Bénéficiaires directs", "56 000", "personnes", "2025", True, True),
        ]
        for program, label, value, unit, period, is_public, is_featured in rows:
            Indicator.objects.update_or_create(
                label=label,
                program=program,
                defaults={
                    "value": value,
                    "unit": unit,
                    "period": period,
                    "is_public": is_public,
                    "is_featured": is_featured,
                },
            )

    def _news(self, programs):
        edu = programs[0]
        now = timezone.now()
        items = [
            {
                "slug": "rentree-scolaire-2025",
                "title": "Rentrée scolaire 2025 — 1 200 kits distribués",
                "excerpt": "Distribution dans 15 villages du Nord.",
                "body": "Les équipes terrain ont finalisé la distribution des kits scolaires.",
                "program": edu,
                "is_staff_only": False,
                "days_ago": 5,
            },
            {
                "slug": "note-interne-audit",
                "title": "[Staff] Note interne — préparation audit Q2",
                "excerpt": "Document réservé au personnel.",
                "body": "Calendrier de collecte des pièces justificatives pour l'audit trimestriel.",
                "program": None,
                "is_staff_only": True,
                "days_ago": 2,
            },
        ]
        for item in items:
            InternalNews.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "title": item["title"],
                    "excerpt": item["excerpt"],
                    "body": item["body"],
                    "program": item["program"],
                    "is_published": True,
                    "is_staff_only": item["is_staff_only"],
                    "published_at": now - timedelta(days=item["days_ago"]),
                },
            )

    def _achievements(self, programs):
        Achievement.objects.update_or_create(
            slug="certification-ecoles",
            defaults={
                "title": "12 écoles certifiées « Espace sûr »",
                "description": "Protocoles WASH et protection de l'enfance déployés.",
                "program": programs[0],
                "date": date.today() - timedelta(days=30),
                "is_published": True,
                "is_staff_only": False,
            },
        )

    def _photos(self, programs):
        for i, program in enumerate(programs[:2], start=1):
            photo, created = Photo.objects.get_or_create(
                title=f"Activité terrain — {program.name}",
                program=program,
                defaults={
                    "caption": f"Séance de terrain — {program.sector}",
                    "is_published": True,
                    "is_staff_only": False,
                    "taken_at": date.today() - timedelta(days=10 * i),
                },
            )
            if created or not photo.image:
                photo.image.save(
                    f"photo-{program.slug}.png",
                    _placeholder_file(f"photo-{program.slug}.png"),
                    save=True,
                )

    def _documents(self, programs):
        from django.core.files.base import ContentFile

        Document.objects.update_or_create(
            title="Rapport annuel 2024 (synthèse)",
            defaults={
                "document_type": Document.DocType.REPORT,
                "summary": "Synthèse des résultats et finances 2024.",
                "program": None,
                "is_published": True,
                "is_private": False,
                "published_at": date(2025, 1, 15),
                "file": ContentFile(
                    b"%PDF-1.4\n% Demo placeholder - remplacer par un vrai PDF\n",
                    name="rapport-annuel-2024.pdf",
                ),
            },
        )
        doc, _ = Document.objects.update_or_create(
            title="[Staff] Procédure achats internes",
            defaults={
                "document_type": Document.DocType.POLICY,
                "summary": "Procédure confidentielle réservée au staff.",
                "program": programs[1],
                "is_published": True,
                "is_private": True,
                "published_at": date.today(),
            },
        )
        if not doc.private_file:
            doc.private_file.save(
                "procedure-achats.pdf",
                ContentFile(
                    b"%PDF-1.4\n% Demo private document\n",
                    name="procedure-achats.pdf",
                ),
                save=True,
            )

    def _dashboard_widgets(self):
        widgets = [
            ("Bénéficiaires cumulés", DashboardWidget.WidgetType.KPI, 1),
            ("Programmes actifs", DashboardWidget.WidgetType.KPI, 2),
            ("Dernières actualités", DashboardWidget.WidgetType.LIST, 3),
        ]
        for title, wtype, order in widgets:
            DashboardWidget.objects.update_or_create(
                title=title,
                defaults={"widget_type": wtype, "order": order, "is_active": True},
            )

    def _demo_staff_user(self):
        user, created = User.objects.get_or_create(
            username=DEMO_STAFF_USERNAME,
            defaults={
                "email": "demo.staff@ong-impact-portal.org",
                "first_name": "Demo",
                "last_name": "Staff",
                "role": User.Role.STAFF,
                "job_title": "Chargé de suivi",
                "department": "Programmes",
                "is_staff": True,
            },
        )
        user.set_password(DEMO_STAFF_PASSWORD)
        user.save()
        staff_group, _ = Group.objects.get_or_create(name="Staff")
        user.groups.add(staff_group)
        self.stdout.write(
            self.style.WARNING(
                f"Compte démo : {DEMO_STAFF_USERNAME} / {DEMO_STAFF_PASSWORD} "
                "(à changer en production)"
            )
        )
