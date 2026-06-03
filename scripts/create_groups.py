from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

GROUPS_PERMISSIONS = {
    'Manager': {
        'programs.program':     ['add','change','delete','view'],
        'documents.document':   ['add','change','delete','view'],
        'statistics.indicator': ['add','change','delete','view'],
        'news.newsarticle':     ['add','change','delete','view'],
    },
    'Staff': {
        'programs.program':    ['view'],
        'documents.document':  ['add','view'],
        'statistics.indicator':['add','view'],
    },
    'Partner': {
        'programs.program':   ['view'],
        'documents.document': ['view'],
    },
}

for group_name, apps_perms in GROUPS_PERMISSIONS.items():
    group, _ = Group.objects.get_or_create(name=group_name)
    for app_model, actions in apps_perms.items():
        app_label, model_name = app_model.split('.')
        ct = ContentType.objects.get(app_label=app_label, model=model_name)
        for action in actions:
            perm = Permission.objects.get(content_type=ct, codename=f'{action}_{model_name}')
            group.permissions.add(perm)
    print(f'Groupe {group_name} configure avec succes')
