# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from registration.models import RegistrationProfile


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'activation_key_expired')
    raw_id_fields = ['user']
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    actions = ['activate_users', 'resend_activation_email',]

    def activate_users(self, request, queryset):
        """
        Activates the selected users, if they are not alrady
        activated.
        
        """
        for profile in queryset:
            RegistrationProfile.objects.activate_user(profile.activation_key)
    activate_users.short_description = _(u"Ativar Usuários")

    def resend_activation_email(self, request, queryset):
        """
        Re-sends activation emails for the selected users.

        Note that this will *only* send activation emails for users
        who are eligible to activate; emails will not be sent to users
        whose activation keys have expired or who have already
        activated.
        
        """
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        for profile in queryset:
            if not profile.activation_key_expired():
                profile.send_activation_email(site)
    resend_activation_email.short_description = _("Re-send activation emails")




class RegistrationUserAdmin(UserAdmin):
    list_display = ('username', 'get_full_name', 'email', 'is_staff', 'get_registration_profile', 'get_group_scout')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    #ordering = ('is_staff')
    list_filter = UserAdmin.list_filter + ('is_active',)

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.allow_tags = True
    get_full_name.short_description = _(u"Nome Completo")

    def get_group_scout(self, obj):
        name = u''
        profile = obj.registrationprofile_set.get()
        if profile:
            name = profile.scout_group
        return name
    get_group_scout.allow_tags = True
    get_group_scout.short_description = _(u"Grupo Escoteiro")

    def get_registration_profile(self, obj):
        link = u''
        profile = obj.registrationprofile_set.get()
        if profile:
            link = '<a href="%s">%s</a>' % (reverse('admin:registration_registrationprofile_change', args=(profile.pk,)), profile.user)
        return link
    get_registration_profile.allow_tags = True
    get_registration_profile.short_description = _(u"Perfil")

admin.site.register(RegistrationProfile, RegistrationAdmin)
admin.site.unregister(User)
admin.site.register(User, RegistrationUserAdmin)