# -*- coding:utf-8 -*-

from django import template
from django.core.urlresolvers import resolve
from django.template.loader import get_template
from django.template import Context
from django.utils.translation import ugettext_lazy as _

register = template.Library()

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
                # 'url_name': 'institution:apresentacao',

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
        # 'url': reverse('institution:parceiros'),
    },
]


@register.simple_tag(takes_context=True)
def create_menu(context):
    """
    Tag que cria o menu principal do projeto
    """
    temp = get_template('institution/menu.html')
    return temp.render(Context({'menu_list': Menu, 'request': context.get('request')}, autoescape=context.autoescape))


@register.simple_tag(takes_context=True)
def create_navigation(context):
    """
    Migalhas
    """
    request = context.get('request')

    path_info = request.META.get('PATH_INFO')
    # links = [Home, ]
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

    temp = get_template('institution/navigation.html')
    return temp.render(
        Context({'navigation_list': links, 'request': context.get('request')}, autoescape=context.autoescape))


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




