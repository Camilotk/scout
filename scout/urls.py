# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
import os

from campotec.auth import login as CampotecLogin, logout as CampotecLogout
from campotec.views import CampotecHomePageView, CampotecSpecialtiesInscriptionView, CampotecInscriptionViews


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # CAMPOTEC
    url(r'^campotec/$', CampotecHomePageView.as_view(), name="campotec-homepage"),
    #Login do Campotec
    #url(r'^login/$', CampotecLogin, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^campotec/login/$', CampotecLogin, {'template_name': 'campotec/login.html'}, name='campotec-login'),
    url(r'^campotec/logout/$', CampotecLogout, name='campotec-logout'),
    # Inscrição em especialidade
    url(r'^campotec/inscricao/$', CampotecSpecialtiesInscriptionView.as_view(), name="campotec-inscription"),
    #url(r'^campotec/inscrever/$', CampotecInscriptionViews.as_view(), name="campotec-add-inscription"),

    url(r'^star_wars/', TemplateView.as_view(template_name='core/star_wars.html'), name='star_wars')

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
    )
