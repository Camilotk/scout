# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from core.admin import activate, inactivate
from scout_group.models import ScoutGroup, UserScoutGroup


class ScoutGroupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'active',)
    search_fields = ('name', 'number', 'uf',)
    ordering = ('active', 'name', 'number', 'uf', '-updated_at',)
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
    )
    actions = [inactivate, activate, ]


class UserScoutGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'scout_group',)
    search_fields = ('user__username', 'scout_group__name', 'scout_group__number', 'scout_group__uf',)
    ordering = ('user', 'scout_group',)


admin.site.register(ScoutGroup, ScoutGroupAdmin)
admin.site.register(UserScoutGroup, UserScoutGroupAdmin)