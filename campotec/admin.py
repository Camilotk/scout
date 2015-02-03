# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.conf import settings
from models import Branch, Specialty, Programation
from core.models import ACTIVE, INACTIVE


def inactivate(self, request, queryset):
    queryset.update(active=INACTIVE)
inactivate.short_description = _(u"Não Exibir / Inativar")


def activate(self, request, queryset):
    queryset.update(active=ACTIVE)
activate.short_description = _(u"Exibir / Ativar")


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'group_link')
    search_fields = ('name', 'description', 'active')
    ordering = ('active', '-updated_at', 'name', 'description')
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
    )
    actions = [inactivate, activate,]

    def group_link(self, obj):
        """
        Cria link para a chave estrangeira do Grupo de Usuario na listagem dos Ramos
        """
        group = Group.objects.get(branch__pk=obj.pk)
        return '<a href="%s">%s</a>' % (reverse('admin:auth_group_change', args=(group.pk,)), group.name)
    group_link.allow_tags = True


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_short', 'date', 'turn', 'num_places', 'num_inscriptions' ,'level_1', 'level_2', 'level_3', 'branch_link', 'active', 'image_thumb')
    #list_display_links = ('name',)
    search_fields = ('name', 'description', 'branch')
    ordering = ('active', 'name', 'description')
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
        'branch',
        ('level_1', admin.BooleanFieldListFilter),
        ('level_2', admin.BooleanFieldListFilter),
        ('level_3', admin.BooleanFieldListFilter),
    )
    actions = [inactivate, activate,]

    def description_short(self, obj):
        """
        Corta o texto da Descrição para nao ficar exibir muito grande na listagem
        """
        if len(obj.description) > 50:
            return "%s..." % obj.description[0:50]
        else:
            return "%s" % obj.description
    description_short.allow_tags = True

    def branch_link(self, obj):
        """
        Cria link para a chave estrangeira do Ramo na listagem de especialidades
        """
        return '<a href="%s">%s</a>' % (reverse('admin:campotec_branch_change', args=(obj.branch.pk,)), obj.branch.name)
    branch_link.allow_tags = True

    def image_thumb(self, obj):
        """
        Exibe miniatura da imagem na listagem
        """
        return '<img src="%s" style="width:50px;">' % (obj.get_image())
    image_thumb.allow_tags = True

    def num_inscriptions(self, obj):
        """
        Exibe a quantidade de inscritos na especialidade
        """
        return len(obj.inscription.all())


class ProgramationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'active', 'description_short', 'image_thumb')
    #list_display_links = ('name',)
    search_fields = ('name', 'description')
    ordering = ('date_time', 'name', 'active', 'description')
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
    )
    actions = [inactivate, activate,]

    def description_short(self, obj):
        """
        Corta o texto da Descrição para nao ficar exibir muito grande na listagem
        """
        if (len(obj.description) > 80):
            return "%s..." % obj.description[0:80]
        else:
            return "%s" % obj.description

    def image_thumb(self, obj):
        """
        Exibe miniatura da imagem na listagem
        """
        return '<img src="%s%s" style="width:50px;">' % (settings.MEDIA_URL, obj.image)
    image_thumb.allow_tags = True

admin.site.register(Branch, BranchAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Programation, ProgramationAdmin)
