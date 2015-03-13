# -*- coding:utf-8 -*-
from copy import deepcopy
from django.contrib.auth.hashers import make_password
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.forms import forms
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

import os
import re
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.conf import settings
from ckeditor.fields import RichTextField
from core.models import CoreModel, CHOICE_ACTIVE, ACTIVE, INACTIVE, get_valid_uf
from registration.models import RegistrationProfile
from scout_group.models import ScoutGroup


class Homepage(CoreModel):
    """
    Pagina inicial
    """
    HOMEPAGE_IMAGE_PATH = os.path.join('campotec', 'homepage')

    homepage_active = models.CharField(verbose_name=_(u"Ativar Página Inicial"), max_length=1, choices=CHOICE_ACTIVE,
                                       default=ACTIVE, blank=False)
    homepage_logo = models.ImageField(verbose_name=_(u"Cabeçalho Logo"), upload_to=HOMEPAGE_IMAGE_PATH, null=True,
                                      blank=True, help_text=_(
            u"Para não distorcer e manter a responsividade, envie uma imagem com resolução média de 300 x 300px."))

    homepage_title = RichTextField(verbose_name=_(u"Cabeçalho Título"), blank=True, config_name='description')
    homepage_image_background = models.ImageField(verbose_name=_(u"Cabeçalho Imagem de Fundo"),
                                                  upload_to=HOMEPAGE_IMAGE_PATH, null=True, blank=True, help_text=_(
            u"Para não distorcer, envie uma imagem com resolução máxima de 200 x 200 px."))

    information_active = models.CharField(verbose_name=_(u"Exibir Bloco Informações"), max_length=1,
                                          choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    information_title = RichTextField(verbose_name=_(u"Informações Título"), config_name='title', null=True, blank=True)
    information_text = RichTextField(verbose_name=_(u"Informações Texto"), config_name='description', null=True,
                                     blank=True)

    local_active = models.CharField(verbose_name=_(u"Exibir Bloco Local"), max_length=1, choices=CHOICE_ACTIVE,
                                    default=ACTIVE, blank=False)
    local_maps_name = models.CharField(verbose_name=_(u"Local no Maps"), max_length=500, blank=True,
                                       help_text=_(u"Nome do Local no Google Maps."))
    local_title = RichTextField(verbose_name=_(u"Local Título"), config_name='title', null=True, blank=True)
    local_text = RichTextField(verbose_name=_(u"Local Texto"), blank=True, config_name='description')

    observation_active = models.CharField(verbose_name=_(u"Exibir Bloco Observações"), max_length=1,
                                          choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)
    observation_title = RichTextField(verbose_name=_(u"Observações Título"), config_name='title', null=True, blank=True)
    observation_text = RichTextField(verbose_name=_(u"Observações Texto"), blank=True, config_name='description')

    class Meta:
        ordering = ["homepage_active"]
        db_table = "campotec_homepage"
        verbose_name = _(u"Página Inicial")
        verbose_name_plural = _(u"Páginas Iniciais")

    def __unicode__(self):
        text = strip_tags(self.homepage_title)
        if len(text) > 50:
            text = "%s..." % text[0:50]
        else:
            text = "%s" % text
        return mark_safe(text)

    def get_url_homepage_preview(self):
        return reverse('campotec-homepage-preview', args=(self.id,))

    def duplicate_save(self):
        obj_new = deepcopy(self)
        obj_new.id = None
        obj_new.homepage_active = INACTIVE
        obj_new.save()
        return obj_new

    def has_more_one_active(self):
        """
        SE possui mais de um registro com homepage_active, retorna True
        SE nao False
        """
        if Homepage.objects.filter(homepage_active=ACTIVE).exclude(id=self.id).count() > 0:
            return True
        else:
            return False

    def is_information_active(self):
        if self.information_active == ACTIVE:
            return True
        else:
            return False

    def is_local_active(self):
        if self.local_active == ACTIVE:
            return True
        else:
            return False

    def is_observation_active(self):
        if self.observation_active == ACTIVE:
            return True
        else:
            return False

    def get_homepage_logo(self):
        if self.homepage_logo:
            return "%s/%s" % (settings.MEDIA_URL, self.homepage_logo)
        else:
            return os.path.join(settings.STATIC_URL, 'campotec', 'img', 'logo.png')

    def get_homepage_image_background(self):
        if self.homepage_image_background:
            return "%s/%s" % (settings.MEDIA_URL, self.homepage_image_background)
        else:
            return os.path.join(settings.STATIC_URL, 'campotec', 'img', 'header.jpg')


class Branch(CoreModel):
    """
    Ramo
    """
    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    description = models.TextField(verbose_name=_(u"Descrição"), max_length=500, blank=True)
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default='Y', blank=False)
    group = models.ForeignKey(verbose_name=_(u"Grupo de Usuário"), to=Group, null=True, blank=True)

    class Meta:
        ordering = ["-name"]
        db_table = "campotec_branch"
        verbose_name = _(u"Ramo")
        verbose_name_plural = _(u"Ramos")

    def __unicode__(self):
        return self.name

    def get_specialties_actives_order_by_name(self):
        return self.specialty_set.filter(active=ACTIVE).order_by('date', 'name')

    def get_specialties_actives_order_by_name_user(self, user):
        specialty_list = self.specialty_set.filter(active=ACTIVE).order_by('date', 'name')
        for specialty in specialty_list:
            specialty.check_inscribed(user)
        return specialty_list

    def remove_all_users(self):
        """
        Remove todos os usuarios associados ao grupo deste Ramo
        """
        for user in self.group.user_set.all():
            user.delete()


    @staticmethod
    def export_xls_users_by_specialty(request, queryset):
        """

        """
        if not request.user.is_staff:
            raise PermissionDenied

        import xlwt
        # inicia o objeto da planilha
        work_book = xlwt.Workbook(encoding='utf-8')
        # cria a planilha
        plan = work_book.add_sheet('plan_1')

        # Configuracoes da planilha
        style_default = xlwt.easyxf(
            'font: name Arial color black; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_colour white;')
        style_title = xlwt.easyxf(
            'font: name Arial, bold True, color white; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_colour black;')
        style_subtitle = xlwt.easyxf(
            'font: name Arial, bold True, color black; borders: left thin, right thin, top thin, bottom thin; pattern: pattern solid, fore_colour white;')

        # Seta tamanho das colunas
        col_n = 0
        plan.col(0).width = 4500
        col_n += 1
        plan.col(col_n).width = 4500
        col_n += 1
        plan.col(col_n).width = 4500
        col_n += 1
        plan.col(col_n).width = 4500
        col_n += 1
        plan.col(col_n).width = 4500

        titles = [u'Especialidade', u'Ramo', u'Dia', u'Data', u'Turno', u'Num. Inscritos', u'Num. Vagas', ]
        subtitles = [u'Registro UEB', u'Nome', u'Grupo/Região', ]
        line_n = 0
        # escrevendo os titulos na primeira linha do arquivo
        for i in range(len(titles)):
            plan.write(line_n, i, titles[i], style_title)
        line_n = 1
        # Escrevendo os subtitulos na segunda linha do arquivo
        for i in range(len(subtitles)):
            plan.write(line_n, i, subtitles[i], style_subtitle)

        for branch in queryset.all():

            for specialty in Specialty.objects.filter(branch=branch).order_by('branch', 'date'):
                line_n += 2
                col_n = 0

                # Escreve o subtitulo com a Especialidade
                plan.write(line_n, col_n, specialty.name, style_title)
                col_n += 1
                plan.write(line_n, col_n, specialty.branch.name, style_title)
                col_n += 1
                plan.write(line_n, col_n, _(specialty.date.strftime('%A')).__unicode__(), style_title)
                col_n += 1
                plan.write(line_n, col_n, specialty.date.strftime('%d/%m/%Y'), style_title)
                col_n += 1
                plan.write(line_n, col_n, specialty.get_turn_display(), style_title)
                col_n += 1
                plan.write(line_n, col_n, specialty.inscription.count(), style_title)
                col_n += 1
                plan.write(line_n, col_n, specialty.num_places, style_title)

                for user in specialty.inscription.all().order_by('first_name', 'last_name'):
                    line_n += 1
                    col_n = 0
                    plan.write(line_n, col_n, user.get_username(), style_default)
                    col_n += 1
                    plan.write(line_n, col_n, user.get_full_name(), style_default)
                    col_n += 1
                    scout_group_name = ''
                    scout_group = user.registrationprofile_set.get().scout_group
                    if scout_group:
                        scout_group_name = scout_group.get_short_name()
                    plan.write(line_n, col_n, scout_group_name, style_default)

            # Lista os usuarios nao inscritos em especialidades
            # list_dont_inscription = branch.group.user_set.exclude(specialty__contains=Specialty.objects.all())
            list_dont_inscription = branch.group.user_set.filter(specialty=None).exclude(
                registrationprofile__scout_group=None)

            if list_dont_inscription:
                line_n += 2
                col_n = 0
                plan.write(line_n, col_n, u"Usuarios NÃO inscritos em especialidades", style_title)
                col_n += 1
                plan.write(line_n, col_n, branch.name, style_title)

                for user in list_dont_inscription:
                    line_n += 1
                    col_n = 0
                    plan.write(line_n, col_n, user.get_username(), style_default)
                    col_n += 1
                    plan.write(line_n, col_n, user.get_full_name(), style_default)
                    col_n += 1
                    scout_group = user.registrationprofile_set.get().scout_group
                    plan.write(line_n, col_n, scout_group.get_short_name(), style_default)

        # work_book.save(file_export)
        return work_book


class Specialty(CoreModel):
    """
    Especialidades
    """
    IMAGE_PATH = os.path.join('campotec', 'specialty')

    TURN_MORNING = 'M'
    TURN_AFTER = 'T'
    TURN_ALL_DAY = 'D'
    CHOICE_TURN = (
        (TURN_MORNING, _(u"Manhã")),
        (TURN_AFTER, _(u"Tarde")),
        (TURN_ALL_DAY, _(u"Manhã e Tarde")),
    )

    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    description = RichTextField(verbose_name=_(u"Descrição"), max_length=1000, blank=True, config_name='description')
    date = models.DateField(verbose_name=_(u"Data"))
    turn = models.CharField(verbose_name=_(u"Turno"), max_length=1, choices=CHOICE_TURN, default=TURN_ALL_DAY,
                            blank=False)
    num_places = models.IntegerField(verbose_name=_(u"Nº de Vagas"), default=0, blank=False, null=False)
    inscription = models.ManyToManyField(to=User, db_table='campotec_specialty_inscription', blank=True)
    level_1 = models.BooleanField(verbose_name=_(u"Nível 1"), default=False)
    level_2 = models.BooleanField(verbose_name=_(u"Nível 2"), default=False)
    level_3 = models.BooleanField(verbose_name=_(u"Nível 3"), default=False)
    branch = models.ForeignKey(verbose_name=_(u"Ramo"), to=Branch, null=False)
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default=ACTIVE,
                              blank=False)
    image = models.ImageField(verbose_name=_(u"Imagem"), upload_to=IMAGE_PATH, null=True, blank=True, help_text=_(
        u"Para não distorcer, envie uma imagem com resolução máxima de 200 x 200 px."))

    is_inscribed = False

    class Meta:
        ordering = ["-name", "-branch"]
        db_table = "campotec_specialty"
        verbose_name = _(u"Especialidade")
        verbose_name_plural = _(u"Especialidades")

    @staticmethod
    def remove_all_inscriptions_user(user):
        specialty_list = Specialty.objects.filter(inscription=user)
        for specialty in specialty_list:
            specialty.inscription.remove(user)

    def __unicode__(self):
        return self.name

    def check_inscribed(self, user=None):
        """
        Checa se o usuario esta inscrito na especialidade
        """
        if user in self.inscription.all():
            self.is_inscribed = True

    def get_image(self):
        if self.image:
            return "%s%s" % (settings.MEDIA_URL, self.image.name)
        else:
            return "%s/campotec/img/especialidade_padrao.jpg" % settings.STATIC_URL


class Programation(CoreModel):
    """
    Programação do Evento
    """
    IMAGE_PATH = os.path.join('campotec', 'programation')

    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    date_time = models.DateTimeField(verbose_name=_(u"Data e Hora"))
    active = models.CharField(verbose_name=_(u"Exibir"), max_length=1, choices=CHOICE_ACTIVE, default='S', blank=False)

    description = RichTextField(verbose_name=_(u"Descrição"), max_length=1000, blank=True, config_name='description')
    # description = models.TextField(verbose_name=_(u"Descrição"), max_length=1000, blank=True)
    #description = tinymce_models.HTMLField(verbose_name=_(u"Descrição"), max_length=1000, blank=True)

    image = models.ImageField(verbose_name=_(u"Imagem"), upload_to=IMAGE_PATH, null=True, blank=True, help_text=_(
        u"Para não distorcer, envie uma imagem com resolução máxima de 200 x 200 px."))

    class Meta:
        ordering = ["-name", "-description"]
        db_table = "campotec_programation"
        verbose_name = _(u"Programação")
        verbose_name_plural = _(u"Programações")

    def __unicode__(self):
        return "%s - %s" % (self.name, self.date_time)


class ImportInscriptions(CoreModel):
    """
    Importação dos arquivos de xls com registros dos usuarios
    """
    IMPORT_INSCRIPTION_FILE_PATH = os.path.join('campotec', 'import_inscription')

    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, blank=True, null=True)
    file = models.FileField(verbose_name=_(u"Arquivo .XLS"), upload_to=IMPORT_INSCRIPTION_FILE_PATH, null=False,
                            blank=False, help_text=_(u"Importe aqui o arquivo .xls com a lista de inscritos."))
    branch = models.ForeignKey(verbose_name=_(u"Ramo"), to=Branch, null=False,
                               help_text=_(u"Ramo ao qual pertencem os registros do arquivo .xls."))

    class Meta:
        ordering = ['updated_at', '-name', '-file']
        db_table = 'campotec_import_inscription'
        verbose_name = _(u"Importação de Inscrições")
        verbose_name_plural = _(u"Importação de Inscrições")

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.file.name

    def get_file_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.file.name)

    def remove_all_groups_for_user(self, user):
        """
        Remove todos os grupos de usuario do usuario recebido
        """
        for group in user.groups.all():
            user.groups.remove(group)

    def import_users(self, file_read, branch):
        """
        Importa Usuários do respectivo ramo recebido em group

        Exemplo expressao regular para pegar o numeral do grupo e região:
            valid_uf = re.compile(r'^(\d{3}|\d{2}|\d{1}) (-|–) ([a-z]{2}|[A-Z]{2})$')
            valid_uf.match('001 - rs')
        """
        group = branch.group

        list_validation = []

        line_number = 1
        for line in self.xlread(file_read):
            line_number += 1
            # Validacoes do formulario
            num_register = ''
            name = ''
            scout_group_number = 0
            scout_group_uf = ''
            try:
                num_register = line[0].split(' - ')[0]
                name = line[1].split(' ')
                first_name = name.pop(0)
                last_name = " ".join(name)

                # Valida numeral do grupo e regiao
                if u'–' in line[2]:
                    arr = line[2].split(u' – ')
                else:
                    arr = line[2].split(u' - ')
                if arr:
                    scout_group_number = arr[0]
                    scout_group_uf = arr[1].upper()

                if num_register and first_name and last_name and scout_group_number and scout_group_uf:
                    list_validation.append({'username': num_register, 'first_name': first_name, 'last_name': last_name,
                                            'group_number': scout_group_number, 'uf': scout_group_uf})
                else:
                    raise forms.ValidationError(u"Arquivo de importação com erro na linha %d." % line_number)
            except:
                raise forms.ValidationError(u"Arquivo de importação com erro na linha %d." % line_number)

        for item in list_validation:
            user_tuple = User.objects.get_or_create(username=item['username'])
            user = user_tuple[0]
            user.first_name = item['first_name']
            user.last_name = item['last_name']
            user.password = make_password(item['username'])
            user.is_active = 1
            user.is_staff = 0
            user.save()

            self.remove_all_groups_for_user(user)
            user.groups.add(group)

            # Cria o RegistrationProfile
            profile = RegistrationProfile.objects.get_or_create_active_user(user)

            # scout_group = ScoutGroup.objects.filter(number=scout_group_number)
            scout_group_tuple = ScoutGroup.objects.get_or_create(number=item['group_number'],
                                                                 uf=get_valid_uf(item['uf']))
            scout_group = scout_group_tuple[0]
            scout_group.active = ACTIVE
            scout_group.save()

            profile.scout_group = scout_group
            profile.save()


            #user_scout_group_tuple = UserScoutGroup.objects.get_or_create(user=user, scout_group=scout_group)
            #print "REG: %s | Grupo: %s - %s " % (user.first_name, line_scout_group[0], line_scout_group[1])

    def xlread(self, file_read):
        # xls = xlrd.open_workbook(file_path)
        import xlrd

        xls = xlrd.open_workbook(file_contents=file_read)
        plan = xls.sheets()[0]
        for i in xrange(1, plan.nrows, 1):
            yield plan.row_values(i)


@receiver(pre_delete, sender=Specialty)
@receiver(pre_delete, sender=Programation)
def delete_image(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando removido o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    instance.image.delete(False)


@receiver(pre_save, sender=Specialty)
@receiver(pre_save, sender=Programation)
def delete_image_on_update(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando atualizado o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    try:
        obj = Specialty.objects.get(id=instance.id)
        if not instance.image.name or (obj.image.file.name != instance.image.file.name):
            # Deleta a imagem
            obj.image.delete(save=False)
    except:
        pass


@receiver(pre_delete, sender=ImportInscriptions)
def import_inscriptions_delete_file(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando removido o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    instance.file.delete(False)


@receiver(pre_save, sender=ImportInscriptions)
def import_inscriptions_delete_file_on_update(sender, instance, **kwargs):
    """
    Signal para deletar arquivo quando atualizado o registro.
    Passar False para o metodo delete para que a instancia não salve o model.
    Usado nos models:
    - Specialty
    - Programation
    """
    try:
        obj = ImportInscriptions.objects.get(id=instance.id)
        if not instance.file.name or (obj.file.file.name != instance.file.file.name):
            # Deleta a imagem
            obj.file.delete(save=False)
    except:
        pass


# @receiver(post_save, sender=ImportInscriptions)
# def import_inscriptions_delete_file_on_update(sender, instance, **kwargs):
# """
#
#     """
#     instance.import_users()
