# ONG Impact Portal — Concept de plateforme

## Nom proposé

**ONG Impact Portal** (nom technique : `ong-impact-portal`)

Slogan suggéré : *« Centraliser l'impact, partager la connaissance institutionnelle »*

## Objectif stratégique

Offrir à une ONG un portail web unique pour :

- valoriser l'impact des programmes auprès des partenaires et donateurs ;
- fédérer la mémoire institutionnelle (documents, rapports, photos, réalisations) ;
- donner au staff un espace privé fiable pour les indicateurs et contenus sensibles ;
- réduire la dispersion des fichiers (drives, e-mails, clés USB).

## Public cible

| Public | Besoin |
|--------|--------|
| Direction & coordination | Vision synthétique, indicateurs, rapports |
| Équipes terrain & programmes | Pages projet, statistiques, photos terrain |
| Communication | Actualités, galerie, pages institutionnelles |
| Partenaires / bailleurs (option) | Transparence sur résultats publics |
| Staff interne | Espace privé, documents confidentiels |

## Modules fonctionnels

1. **Institutionnel** (`core`) — accueil, à propos, pages CMS
2. **Programmes** (`programs`) — fiches projet, KPI liés
3. **Contenus** (`content`) — actualités, réalisations, galerie
4. **Documents** (`documents`) — bibliothèque publique + fichiers privés
5. **Tableaux de bord** (`dashboards`) — accueil staff, widgets
6. **Comptes** (`accounts`) — auth, profils, rôles

## Pages publiques

- Accueil (programmes phares, KPI, actualités, photos)
- Liste & fiche programme
- Indicateurs de performance
- Actualités, réalisations, galerie
- Documents institutionnels publics
- À propos & pages institutionnelles (`/pages/<slug>/`)

## Espace privé (staff)

- `/comptes/connexion/` — authentification
- `/tableaux-de-bord/` — accueil staff
- `/tableaux-de-bord/vue-generale/` — tableau de bord
- `/documents/staff/` — tous les documents dont privés
- `/fichiers-prives/telecharger/<id>/` — téléchargement sécurisé
- `/admin/` — gestion des contenus

## Rôles utilisateurs

| Groupe Django | Permissions typiques |
|---------------|----------------------|
| **SuperAdmin** | Administration complète |
| **Communicator** | Actualités, médias, pages |
| **ProgramManager** | Programmes, indicateurs, rapports |
| **Staff** | Lecture espace privé |

## Types de contenus

- Programmes / projets avec image de couverture
- Indicateurs (KPI) publics ou internes
- Actualités (publiques ou `is_staff_only`)
- Réalisations internes
- Photos d'activités
- Documents (institutionnel, rapport, politique) publics ou privés
- Widgets de tableau de bord (JSON config)

## Navigation

```
Accueil → Programmes → [Fiche programme]
         → Indicateurs
         → Actualités / Réalisations / Galerie
         → Documents
         → À propos
[Connexion staff] → Tableau de bord → Documents staff / Admin
```

## Architecture générale

```
[Navigateur]
     ↓ HTTPS
[Gunicorn + WhiteNoise]
     ↓
[Django 5 — apps métier]
     ↓
[SQLite dev | PostgreSQL prod]
[Fichiers media/ + private_media/]
```

Séparation **development** / **production** via `config/settings/`.
