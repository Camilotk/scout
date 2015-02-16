# -*- coding:utf-8 -*-
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password

from core.models import ACTIVE, INACTIVE
from models import Branch, Homepage

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

# Homepages cadastrados
HOMEPAGES = [
    {
        'homepage_active': ACTIVE,
        'homepage_logo': None,
        'homepage_title': u"25 e 26 de Abril de 2015 • Parque Saint-Hilaire",
        'homepage_image_background': None,
        'information_active': ACTIVE,
        'information_title': u"INFORMAÇÕES GERAIS",
        'information_text': u"""
            <p>O Campotec - Acampamento Técnico de Especialidades - é uma atividade que visa desenvolver habilidades nos jovens lobinhos(as), escoteiros(as), seniors e guias, para uma futura obtenção de especialidades.</p>
            <p>Todos os participantes (jovens, escotistas e pessoal de apoio) acamparão. Não haverá espaço para acantonamento.</p>
            <p>A alimentação é de responsabilidade do Grupo Escoteiro e para isso, serão oferecidos quiosques para utilização de um ou mais Grupos Escoteiros.</p>
            <p>Após o encerramento das inscrições todos os participantes receberão informações em seu endereço eletrônico sobre as atividades oferecidas no evento.</p>
            <p>Serão observadas todas as regras de segurança, bem como todas as resoluções previstas para o bom andamento da atividade, sendo então proibido o consumo de bebidas alcoólicas, perturbação de ambiente e evitar o fumo na frente dos jovens, principalmente, durante as atividades."</p>
            """,
        'local_active': ACTIVE,
        'local_maps_name': u"Avenida Senador Salgado Filho, 2785 - Viamão",
        'local_title': u"LOCAL",
        'local_text': u"Campo Escola Escoteiro - João Ribeiro do Santos | Parque Saint-Hilaire <br> Avenida Senador Salgado Filho, 2785 • Viamão • Centro • RS",
        'observation_active': ACTIVE,
        'observation_title': u"INSCRIÇÕES",
        'observation_text': u"""
            <p style="text-align:justify">A inscrição de todos participantes deve ocorrer através do&nbsp;<a href="http://sigue.escoteiros.org.br/siguejovem" style="box-sizing: border-box; color: rgb(38, 107, 160); text-decoration: none; background: transparent;" target="_blank">Meu Sigue</a>, nas opções (Jovem, Adulto ou Equipe de Serviço).</p>
            <p style="text-align:justify">Os jovens e adultos deverão encaminhar suas fichas de inscrição do SIGUE devidamente autorizados. O limite para inscrição é 24/04.</p>
            <p style="text-align:justify">O valor de inscrição dos jovens é de R$ 25,00.</p>
            <p style="text-align:justify">O jovem após se inscrever, irá escolher as especialidades oferecidas, através de formulário online cujo endereço seja enviado por e-mail. Cada jovem participará de oficinas de especialidade, conforme o que o seu ramo oferecer.</p>
            <p style="text-align:justify">O período de inscrição para a Equipe de Serviço estará disponível no no Meu Sigue entre 24/03 e 24/04, com valor de R$ 15,00 (cobre certificado, distintivo do evento). Alimentação não inclusa!</p>
            <p style="text-align:justify">Os escotistas acompanhantes receberão capacitação para trabalhar com especialidades e fichas de atividades, bem como a avaliação de níveis conquistados pelos jovens.</p>
            <p style="text-align:justify">Os membros das equipes de apoio dos Grupos Escoteiros participantes ingressarão no evento pagando a taxa de uso do parque que é R$ 15,00 (Taxa de uso + lembrança do evento), devendo ser paga no campo escola.</p>
            <p style="text-align:justify">Os Grupos Escoteiros participantes devem identificar seus colaboradores através de um e-mail para secretaria@escoteirosrs.org.br com o titulo de: Informação apoio Campotec 2014 + Numeral e nome do GE, e no corpo de email a relação das pessoas com Nome, RG e Celular até o dia 15 de maio.</p>
            """,
    }
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
        user_new.is_staff = 1
        user_new.save()
        group = Group.objects.get(name=u'Escoteiro')
        group.user_set.add(user_new)

    def create_branches(self):
        """
        Cadastra os Ramos
        """
        #print("CADASTRAR RAMOS:")
        for branch in BRANCHS:
            branch_new = Branch()
            branch_new.id = branch['id']
            branch_new.name = branch['name']
            branch_new.description = branch['description']
            branch_new.active = branch['active']
            if branch.get('group'):
                branch_new.group = Group.objects.get(pk = branch['group']['id'])
            branch_new.save()
            #print("...Ramo: %d - %s Salvo." % (branch_new.id, branch_new.name))

    def create_homepages(self):
        """
        Cadastra as HOMEPAGES
        """
        for item in HOMEPAGES:
            homepage = Homepage()
            homepage.homepage_active = item['homepage_active']
            homepage.homepage_logo = item['homepage_logo']
            homepage.homepage_title = item['homepage_title']
            homepage.homepage_image_background = item['homepage_image_background']
            homepage.information_active = item['information_active']
            homepage.information_title = item['information_title']
            homepage.information_text = item['information_text']
            homepage.local_active = item['local_active']
            homepage.local_maps_name = item['local_maps_name']
            homepage.local_title = item['local_title']
            homepage.local_text = item['local_text']
            homepage.observation_active = item['observation_active']
            homepage.observation_title = item['observation_title']
            homepage.observation_text = item['observation_text']
            homepage.save()
