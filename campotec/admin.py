# -*- coding:utf-8 -*-
from django.contrib.admin import helpers
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.conf import settings
from core.models import INACTIVE
from campotec.forms import ImportInscriptionsForm, HomepageForm
from models import Homepage, Branch, Specialty, Programation, ImportInscriptions
from core.admin import activate, inactivate


class HomepageAdmin(admin.ModelAdmin):
    list_display = ('id', 'homepage_title_short', 'homepage_active', 'information_active', 'local_active', 'observation_active')
    list_display_links = ('id', 'homepage_title_short', 'homepage_active',)
    actions = ('duplicate_item',)

    form = HomepageForm

    def homepage_title_short(self, obj):
        """
        Retorna o titulo sem tags html para a exibição na listagem
        """
        return obj.__unicode__()
    homepage_title_short.allow_tags = True

    def duplicate_item(self, request, queryset):
        if queryset.count() <> 1:
            self.message_user(request, _(u"Selecione apenas 1 item para duplicar"), level=messages.ERROR)
        else:
            obj = queryset.get()
            obj_new = obj.duplicate_save()
            return HttpResponseRedirect(redirect_to=reverse('admin:campotec_homepage_change', args=(obj_new.id,)))
    duplicate_item.short_description = _(u"Duplicar Item")


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'group_link')
    search_fields = ('name', 'description')
    ordering = ('active', '-updated_at', 'name', 'description')
    list_filter = (
        ('active', admin.ChoicesFieldListFilter),
    )

    def group_link(self, obj):
        """
        Cria link para a chave estrangeira do Grupo de Usuario na listagem dos Ramos
        """
        group = Group.objects.get(branch__pk=obj.pk)
        return '<a href="%s">%s</a>' % (reverse('admin:auth_group_change', args=(group.pk,)), group.name)
    group_link.allow_tags = True

    def export_users_for_branchs(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=export_iscritos.xls'
        work_book = Branch.export_xls_users_by_specialty(request, queryset)
        work_book.save(response)
        return response
    export_users_for_branchs.short_description = _(u"Exportar Usuários por Ramo - em excel (.xls)")

    def remove_users_for_branch(self, request, queryset):
        if request.POST.get('post'):
            # Executa a remocao
            for branch in queryset.all():
                branch.remove_all_users()
        else:
            context = {
                'title': _("Are you sure?"),
                'queryset': queryset,
                'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
                'opts': self.model._meta,
                'name_plural': self.model._meta.verbose_name_plural,
                'action_name': "remove_users_for_branch",
            }
            return TemplateResponse(request, 'core/admin/confirmation_delete.html', context, current_app=self.admin_site.name)

    remove_users_for_branch.short_description = _(u"Remover usuários por ramo.")

    actions = [inactivate, activate, export_users_for_branchs, remove_users_for_branch, ]


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_short', 'date', 'turn', 'num_places', 'num_inscriptions' ,'level_1', 'level_2', 'level_3', 'branch_link', 'active', 'image_thumb')
    #list_display_links = ('name',)
    search_fields = ('name', 'description')
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
        text = strip_tags(obj.description)
        if len(text) > 50:
            return "%s..." % text[0:50]
        else:
            return "%s" % text
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
    actions = [inactivate, activate, ]

    def description_short(self, obj):
        """
        Corta o texto da Descrição para nao ficar exibir muito grande na listagem
        """
        text = strip_tags(obj.description)
        if (len(text) > 80):
            return "%s..." % text[0:80]
        else:
            return "%s" % text

    def image_thumb(self, obj):
        """
        Exibe miniatura da imagem na listagem
        """
        return '<img src="%s%s" style="width:50px;">' % (settings.MEDIA_URL, obj.image)
    image_thumb.allow_tags = True


class ImportInscriptionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated_at', 'file_link']
    search_fields = ('name', 'file')
    ordering = ('-updated_at',)
    form = ImportInscriptionsForm

    def file_link(self, obj):
        """
        Cria link para a listagem do arquivo
        """
        return '<a href="%s%s" title="%s">%s</a>' % (settings.MEDIA_URL, obj.file, unicode(_(u"Download do arquivo")), obj.file)
    file_link.allow_tags = True


admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Programation, ProgramationAdmin)
admin.site.register(ImportInscriptions, ImportInscriptionsAdmin)



# Para criar uma ação no Cadastro de usuarios:
# def import_users_campotec(self, request, queryset):
#     pass
# import_users_campotec.short_description = _(u"Importar Usuários Campotec")
#
# admin.ModelAdmin.import_users_campotec = import_users_campotec
# admin.ModelAdmin.actions = ['import_users_campotec', ]