# -*- coding:utf-8 -*-
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password

from models import Branch

# Grupos de usuários
GROUPS = [
    {'id': 1, 'name': u"Admin"},
    {'id': 2, 'name': u"Lobinho"},
    {'id': 3, 'name': u"Escoteiro"},
    {'id': 4, 'name': u"Sênior"},
]

# Ramos cadastrados e atrelados aos Grupos
BRANCHS = [
    {'id': 1, 'name': u"Ramo Lobinho", 'description': '', 'active': 'Y', 'group': GROUPS[1]},
    {'id': 2, 'name': u"Ramo Escoteiro", 'description': '', 'active': 'Y', 'group': GROUPS[2]},
    {'id': 3, 'name': u"Ramo Sênior", 'description': '', 'active': 'Y', 'group': GROUPS[3]},
]


# Cria usuarios para inscrição nas especialidades
class InitialCampotec(object):
    """
    Executar os metodos abaixo ao instalar o app
    - create_groups_user

    """
    def create_groups_user(self):
        """
        Cadastra os novos grupos de usuário
        """
        for group in GROUPS:
            group_new = Group()
            group_new.pk = group['id']
            group_new.name = group['name']
            group_new.save()

    def create_users(self):
        """
        Cadastra os usuários para inscrição em especialidades
        """
        user_new = User()
        user_new.name = 'Usuário 123'
        user_new.password = make_password('123')
        user_new.username = '123'
        user_new.first_name = 'Nome 1'
        user_new.last_name = 'Nome 2'
        user_new.email = '123@email.com'
        user_new.is_active = 1
        user_new.is_staff = 0
        user_new.save()
        group = Group.objects.get(name=u'Escoteiro')
        group.user_set.add(user_new)

    def create_branches(self):
        """
        Cadastra os Ramos
        """
        print("CADASTRAR RAMOS:")
        for branch in BRANCHS:
            branch_new = Branch()
            branch_new.id = branch['id']
            branch_new.name = branch['name']
            branch_new.description = branch['description']
            branch_new.active = branch['active']
            if branch.get('group'):
                branch_new.group = Group.objects.get(pk = branch['group']['id'])
            branch_new.save()
            print("...Ramo: %d - %s Salvo." % (branch_new.id, branch_new.name))




