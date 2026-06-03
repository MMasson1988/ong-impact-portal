# ImpactBase - Portail ONG (ong-impact-portal)

Plateforme web Django pour centraliser statistiques, documents, rapports
et informations institutionnelles d'une ONG.

## Stack technique
- Python 3.12 / Django 5.1
- PostgreSQL (prod) / SQLite (dev)
- Whitenoise + Gunicorn
- Render.com (hebergement gratuit)

## Installation locale

```bash
git clone https://github.com/MMasson1988/ong-impact-portal.git
cd ong-impact-portal
python -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py shell < scripts/create_groups.py
python manage.py runserver
```

## Roles
| Role | Acces |
|------|-------|
| super_admin | Total |
| manager | Gestion contenu + rapports confidentiels |
| staff | Upload, saisie stats |
| partner | Lecture documents partages |
| public | Pages publiques uniquement |

## Deploiement
Push sur main => GitHub Actions => Tests => Deploy Render.com auto.

## Securite
- SECRET_KEY jamais dans Git (.env)
- DEBUG=False en production
- HTTPS force (HSTS)
- Fichiers prives via vues Django securisees
- Protection brute-force (django-axes)
