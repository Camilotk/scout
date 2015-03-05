# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import InstitutionHomepageView

urlpatterns = patterns('',

    url(r'^$', InstitutionHomepageView.as_view(), name="homepage"),
    url(r'^escotismo/$', TemplateView.as_view(template_name="institution/escotismo.html"), name="escotismo"),
    url(r'^transparencia/$', TemplateView.as_view(template_name="institution/transparencia.html"), name="transparencia"),
    url(r'^institucional/$', TemplateView.as_view(template_name="institution/content.html"), name="institucional"),
    url(r'^diretoria-regional/$', TemplateView.as_view(template_name="institution/diretoria-regional.html"), name="diretoria-regional"),
    url(r'^campo-escola/$', TemplateView.as_view(template_name="institution/campo-escola.html"), name="campo-escola"),
    url(r'^distritos/$', TemplateView.as_view(template_name="institution/distritos-escoteiros.html"), name="distritos"),
    url(r'^distritos/distritos-escoteiros-ajax.html/$', TemplateView.as_view(template_name="institution/distritos-escoteiros-ajax.html"), name="distritos-ajax"),
    url(r'^distritos/distritos-detalhe.html/$', TemplateView.as_view(template_name="institution/distritos-detalhe.html"), name="distritos-detalhe"),
    url(r'^mapa-site/$', TemplateView.as_view(template_name="institution/mapa-site.html"), name="mapa-site"),

    url(r'^content/$', TemplateView.as_view(template_name="institution/content.html"), name="content"),
    url(r'^equipes-regionais/$', TemplateView.as_view(template_name="institution/equipes-regionais.html"), name="equipes-regionais"),

)
