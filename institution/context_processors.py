# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse, resolve, Resolver404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


Home = {
    'name': "Home",
    'url': reverse('institution:homepage'),
}



Menu = [
    {
        'name': "Home",
        'url_name': 'institution:homepage',
    },
    {
        'name': _(u"Escotismo"),
        'url_name': 'institution:escotismo',
    },
    {
        'name': _(u"Transparência"),
        'url_name': 'institution:transparencia',

    },
    {
        'name': _(u"Institucional"),
        'url_name': 'institution:institucional',

        'submenu': [
            {
                'name': _(u"Escotismo"),
                'url_name': 'institution:escotismo',

            },
            {
                'name': _(u"Apresentação"),
                #'url_name': 'institution:apresentacao',

            },
            {
                'name': _(u"Diretoria Regional"),
                'url_name': 'institution:diretoria-regional',

            },
        ]
    },
    {
        'name': _(u"Mapa do Site"),
        'url_name': 'institution:mapa-site',

    },
    {
        'name': _(u"Parceiros"),
        #'url': reverse('institution:parceiros'),
    },
]

# <li><a href="{% url 'institution-content' %}">Missão, Visão e Valores</a></li>
# <li><a href="{% url 'institution-diretoria-regional' %}">Diretoria Regional</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Comissão Fiscal Regional</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Comissão de Ética e Disciplina</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Coordenadorias Regionais</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Comissários Distritais</a></li>
# <li><a href="{% url 'institution-campo-escola' %}">Campo Escola</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Condecorações e Homenagens</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Formação</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Imagem e Comunicação</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Equipe de Método Educativo</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Equipe Pioneira</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Rede de Jovens</a></li>
# <li><a href="{% url 'institution-distritos' %}">Distritos Escoteiros</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Rede de Jovens</a></li>
# <li><a href="{% url 'institution-equipes-regionais' %}">Equipe do Escritório</a></li>


def menu_loader(request):
    """
    Monta o menu principal
    """

    return {'MENU': Menu}


def navigation_teste(request):
    return {}


def navigation(request):
    """
    Migalhas
    """

    path_info = request.META.get('PATH_INFO')
    #links = [Home, ]
    links = []
    list_path = path_info.split('/')
    print(list_path)
    path = '/'

    for link in list_path:
        if link:
            path = "%s%s/" % (path, link)

            try:
                url = resolve(path)
            except Exception:
                url = ''

            if url:
                links.extend(find_url_name_in_menu(url))
            else:
                url = resolve(path_info)
                links = []
                links.append(Menu[0])
                links.append({
                    'name': (list_path[-1] or list_path[-2]).title(),
                    'url_name': url.url_name,
                    'url': path_info,
                })
                break




    return {"NAVIGATION": links}


def find_url_name_in_menu(url):
    links = []
    for menu in Menu:
        if menu.get('url_name') == add_namespace(url.url_name):
            links.append(menu)
            break
        elif menu.get('submenu'):
            for submenu in menu.get('submenu'):
                if submenu.get('url_name') == add_namespace(url.url_name):
                    links.append(menu)
                    links.append(submenu)
                    break

    if not links:
        links.append({
            'name': url.url_name.title(),
            'url_name': url.url_name,
        })
    return links

def add_namespace(url_name):
    return "institution:%s" % (url_name)