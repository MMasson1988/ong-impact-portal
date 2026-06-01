# ONG Impact Portal

Portail web Django pour ONG : centraliser statistiques de programmes, photos, réalisations, rapports, documents institutionnels et espace staff sécurisé.

## Objectif du projet

**ONG Impact Portal** (`ong-impact-portal`) permet à une organisation de :

- publier des informations institutionnelles et des indicateurs d'impact ;
- structurer les contenus par programme ;
- réserver documents et actualités sensibles à l'espace staff ;
- administrer le tout via l'interface Django Admin.

Voir aussi : [docs/CONCEPT.md](docs/CONCEPT.md) et [docs/guide-technique.html](docs/guide-technique.html).

## Prérequis

- Python 3.11+ (testé avec 3.12/3.14)
- Git
- (Production) PostgreSQL 14+

## Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-org/ong-impact-portal.git
cd ong-impact-portal
```

### 2. Environnement virtuel

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 3. Dépendances

```bash
pip install -r requirements.txt
# Optionnel : outils de dev
pip install -r requirements-dev.txt
```

### 4. Configuration `.env`

```bash
cp .env.example .env
```

Éditez `.env` : générez une `SECRET_KEY` forte (ex. `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`).

Variables minimales en développement :

```env
SECRET_KEY=votre-cle-secrete-longue
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SETTINGS_MODULE=config.settings.development
```

### 5. Base de données

```bash
python manage.py migrate
python manage.py setup_roles
python manage.py createsuperuser
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

- Site : http://127.0.0.1:8000/
- Admin : http://127.0.0.1:8000/admin/
- Connexion staff : http://127.0.0.1:8000/comptes/connexion/

Assignez le superutilisateur au groupe **SuperAdmin** dans l'admin (Utilisateurs → groupes).

### Données de démonstration

```bash
python manage.py setup_roles
python manage.py load_demo_data --with-staff-user
```

Crée programmes, indicateurs, actualités, photos, documents et un compte staff de test :

| Champ | Valeur |
|-------|--------|
| Identifiant | `demo.staff` |
| Mot de passe | `DemoONG2026!` |

Relançable sans doublons. Ne pas utiliser ce compte en production.

## Gestion des médias

| Dossier | Usage |
|---------|--------|
| `media/` | Images publiques (programmes, galerie, avatars) |
| `private_media/` | Fichiers confidentiels — servis uniquement via `/fichiers-prives/telecharger/<id>/` |

En développement, les médias publics sont servis par Django si `DEBUG=True`. En production, configurez un stockage objet (S3, Azure Blob) ou un reverse proxy ; ne exposez jamais `private_media/` en URL statique.

## Structure du projet

```
ong-impact-portal/
├── config/                 # Projet Django (urls, wsgi, settings/)
│   └── settings/
│       ├── base.py
│       ├── development.py   # SQLite, DEBUG
│       └── production.py    # PostgreSQL, sécurité
├── apps/
│   ├── accounts/           # User custom, auth, rôles
│   ├── core/               # Accueil, pages institutionnelles
│   ├── programs/           # Programmes & indicateurs
│   ├── content/            # Actualités, réalisations, photos
│   ├── documents/          # Documents publics/privés
│   └── dashboards/         # Espace staff & widgets
├── templates/
├── static/
├── media/ / private_media/
├── .github/workflows/      # CI & déploiement
├── requirements.txt
└── manage.py
```

## Rôles utilisateurs

| Groupe | Accès |
|--------|--------|
| SuperAdmin | Tout + admin Django |
| Communicator | Contenus & communication |
| ProgramManager | Programmes & indicateurs |
| Staff | Lecture espace privé |

Commande : `python manage.py setup_roles`

## Déploiement automatique

### Option recommandée (gratuite / faible coût)

**Render.com** (web service + PostgreSQL free tier) — voir `render.yaml` et `Procfile`.

### CI/CD GitHub Actions

1. **CI** (`.github/workflows/ci.yml`) : `check`, `makemigrations --check`, `migrate` sur chaque PR/push.
2. **Deploy** (`.github/workflows/deploy.yml`) : build, `collectstatic`, webhook Render (`RENDER_DEPLOY_HOOK`).

### Étapes typiques sur le serveur

```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py setup_roles
# Redémarrer Gunicorn / service systemd
sudo systemctl restart gunicorn-ong-portal
```

### Migrations automatiques

Exécutez `migrate --noinput` dans le pipeline ou le script de déploiement **avant** de redémarrer l'application. Sauvegardez la base avant les migrations majeures.

### Fichiers statiques

WhiteNoise sert les fichiers collectés dans `staticfiles/` :

```bash
python manage.py collectstatic --noinput
```

### Redémarrage

- **Render** : redémarrage automatique après deploy hook.
- **VPS** : `systemctl restart gunicorn-ong-portal` ou équivalent.

## Maintenance

- Mettre à jour les dépendances : `pip list --outdated`, tester en staging.
- Surveiller l'espace disque `media/` et `private_media/`.
- Réviser les comptes staff inactifs trimestriellement.

## Sauvegarde

- **Base** : dump PostgreSQL quotidien (`pg_dump`).
- **Fichiers** : synchronisation `media/` + `private_media/` vers stockage externe chiffré.
- Conserver 30 jours minimum ; tester la restauration semestriellement.

## Sécurité

- Ne jamais committer `.env` ni `SECRET_KEY`.
- `DEBUG=False` en production ; `ALLOWED_HOSTS` et `CSRF_TRUSTED_ORIGINS` stricts.
- HTTPS obligatoire (voir `production.py`).
- Fichiers privés : uniquement via `PrivateFileDownloadView` + groupe Staff.
- CSRF activé sur tous les formulaires (`{% csrf_token %}`).
- Principe du moindre privilège pour les groupes Django.

## Versioning

| Branche | Usage |
|---------|--------|
| `main` | Production stable |
| `develop` | Intégration |
| `feature/*` | Fonctionnalités |

**Commits** : Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).

**Tags** : `v0.1.0`, `v0.2.0` — voir [CHANGELOG.md](CHANGELOG.md).

**Workflow GitHub** : PR vers `develop` → revue → merge → release vers `main` → tag → déploiement auto.

## Licence

À définir par l'ONG (MIT, AGPL ou propriétaire interne).
