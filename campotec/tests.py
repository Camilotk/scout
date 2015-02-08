# -*- coding:utf-8 -*-
from django.contrib.auth.hashers import make_password

from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.contrib.auth.models import User, Group
from core.models import GROUP_ESCOTEIRO, GROUP_LOBINHO, GROUP_SENIOR, ACTIVE, get_valid_uf
from campotec.models import Branch, ImportInscriptions, Specialty
from campotec.forms import ImportInscriptionsForm
from scout_group.models import ScoutGroup, UserScoutGroup
from campotec.initial_campotec import InitialCampotec
from datetime import datetime
import os


class CampotecHomePageTest(TestCase):

    def test_details(self):
        response = self.client.get('/campotec/')
        self.assertEqual(response.status_code, 200)



class CampotecImportInscriptionsTest(TestCase):

    def setUp(self):
        initial_campotec = InitialCampotec()
        initial_campotec.create_groups_user()
        initial_campotec.create_users()
        initial_campotec.create_branches()

        self.client = Client()

        self.file_import_inscription = os.path.join(settings.BASE_DIR, 'campotec', 'tests', 'teste_escoteiros.xls')
        self.file_export_inscription = os.path.join(settings.BASE_DIR, 'campotec', 'tests', 'teste_exportacao.xls')

        self.create_specialties()
        self.import_inscription()

    # def test_login(self):
    #     response = self.client.login(username="guerra", password="g")
    #     self.assertTrue(response)

    def import_inscription(self):
        """
        Testa a importação do arquivo xls para o ramo escoteiro.
        """
        branch = Branch.objects.get(name=u"Ramo Escoteiro")
        upload_file = open(self.file_import_inscription, 'r')
        form_data = {
            'name': "Teste 1",
            'branch': branch.pk,
        }
        form_data_file = {'file': SimpleUploadedFile(upload_file.name, upload_file.read()),}

        form = ImportInscriptionsForm(data=form_data,files=form_data_file)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(ImportInscriptions.objects.count(), 1)
        self.assertEqual(User.objects.count(), 335)
        self.inscription_users()


    def create_specialties(self):
        """
        Cria especialidades para utilizar nos testes
        """

        branch_escoteiro = Branch.objects.get(name='Ramo Escoteiro')

        LIST_SPECIALTIES = [
            # PRIMEIRO DIA
            {'id': 1, 'name': u'Primeiros Socorros', 'description': '', 'date': datetime(2015, 3, 7), 'turn': Specialty.TURN_MORNING,
                'num_places': 5, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },
            {'id': 2, 'name': u'Coleções', 'description': '', 'date': datetime(2015, 3, 7), 'turn': Specialty.TURN_AFTER,
                'num_places': 5, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },
            {'id': 3, 'name': u'Pioneiria', 'description': '', 'date': datetime(2015, 3, 7), 'turn': Specialty.TURN_ALL_DAY,
                'num_places': 5, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },

            # SEGUNDO DIA
            {'id': 4, 'name': u'Informática', 'description': '', 'date': datetime(2015, 3, 8), 'turn': Specialty.TURN_MORNING,
                'num_places': 10, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },
            {'id': 5, 'name': u'Fotografia', 'description': '', 'date': datetime(2015, 3, 8), 'turn': Specialty.TURN_AFTER,
                'num_places': 9, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },
            {'id': 6, 'name': u'Sapador', 'description': '', 'date': datetime(2015, 3, 8), 'turn': Specialty.TURN_ALL_DAY,
                'num_places': 8, 'level_1': True, 'branch': branch_escoteiro, 'active': ACTIVE, },
        ]

        for item in LIST_SPECIALTIES:
            Specialty.objects.create(id=item['id'], name=item['name'], description=item['description'], date=item['date'], turn=item['turn'],
                num_places=item['num_places'], level_1=item['level_1'], branch=item['branch'], active=item['active'])

        self.assertEqual(Specialty.objects.count(), len(LIST_SPECIALTIES))

    def inscription_users(self):
        """
        Numero de registro dos usuarios importados no teste:
            770115
            819519
            738795
            593754
            697030
        """
        # Adrian Silva do Nascimento
        user = User.objects.get(username='770115')
        user.specialty_set.add(Specialty.objects.get(id=1)) #primeiros socorros - manha
        user.specialty_set.add(Specialty.objects.get(id=2)) # Coleções - tarde
        user.specialty_set.add(Specialty.objects.get(id=6)) # Sapador - dia inteiro
        self.assertEqual(user.specialty_set.count(), 3)

        # ALESSANDRO RIBEIRO DORNELES
        user = User.objects.get(username='819519')
        user.specialty_set.add(Specialty.objects.get(id=3)) # Pioneiria - dia inteiro
        user.specialty_set.add(Specialty.objects.get(id=4)) # Informatica - manha
        user.specialty_set.add(Specialty.objects.get(id=5)) # Fotografia - tarde
        self.assertEqual(user.specialty_set.count(), 3)

        # BRUNO BECKER SILVA
        user = User.objects.get(username='738795')
        user.specialty_set.add(Specialty.objects.get(id=1)) # Primeiros socorros - manha
        user.specialty_set.add(Specialty.objects.get(id=2)) # coleções - tarde
        user.specialty_set.add(Specialty.objects.get(id=4)) # Informatica - manhã
        user.specialty_set.add(Specialty.objects.get(id=5)) # Fotografia - tarde
        self.assertEqual(user.specialty_set.count(), 4)

        # CAIO MOREIRA LEME
        user = User.objects.get(username='593754')
        user.specialty_set.add(Specialty.objects.get(id=3)) # Pioneiria - dia inteiro
        user.specialty_set.add(Specialty.objects.get(id=6)) # Sapador - dia inteiro
        self.assertEqual(user.specialty_set.count(), 2)

        # Luiza Schiller Beliziario Conceição - SEM ESPECIALIDADES CADASTRADAS



    def test_export_inscriptions(self):
        """
        Testa a exportação dos usuários inscritos em especialidades
        """
        branch = Branch.objects.get(name='Ramo Escoteiro')
        branch.export_xls_users_by_specialty(self.file_export_inscription)


