# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from campotec.auth import login as CampotecLogin, logout as CampotecLogout
from campotec.views import CampotecHomePageView, CampotecSpecialtiesInscriptionView, CampotecHomepagePreview

urlpatterns = patterns('',
                       url(r'^$', CampotecHomePageView.as_view(), name="campotec-homepage"),
                       # Login do Campotec
                       url(r'^login/$', CampotecLogin, {'template_name': 'campotec/login.html'}, name='campotec-login'),
                       url(r'^logout/$', CampotecLogout, name='campotec-logout'),
                       # Inscrição em especialidade
                       url(r'^inscricao/$', CampotecSpecialtiesInscriptionView.as_view(), name="campotec-inscription"),
                       url(r'^preview-homepage/(?P<id>\d+)/$', CampotecHomepagePreview.as_view(),
                           name="campotec-homepage-preview"),
)
