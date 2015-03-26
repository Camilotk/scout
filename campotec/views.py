# -*- coding:utf-8 -*-
from django.http import JsonResponse, HttpResponse, Http404

from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, FormView, TemplateView
from django.conf import settings

from auth import LoginForm, campotec_login_required, campotec_permission_required
from models import Branch, Programation, Specialty, Homepage
from core.models import ACTIVE
import json


class CampotecHomePageView(TemplateView):
    """
    URL: http://g1.globo.com/dynamo/economia/rss2.xml
    """

    template_name = "campotec/homepage.html";
    object = Branch
    queryset = []

    def get(self, request, *args, **kwargs):
        return super(CampotecHomePageView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CampotecHomePageView, self).get_context_data(**kwargs)
        context.update({
            'homepage': Homepage.objects.get(homepage_active=ACTIVE),
            'form': LoginForm(),
            'branch_list': Branch.objects.filter(active=ACTIVE).order_by('-updated_at'),
            'programation_list': Programation.objects.filter(active=ACTIVE).order_by('date_time'),
        })
        return context


class CampotecHomepagePreview(TemplateView):

    template_name = 'campotec/homepage_preview.html'

    @method_decorator(campotec_permission_required('campotec.change_homepage'))
    def dispatch(self, *args, **kwargs):
        return super(CampotecHomepagePreview, self).dispatch(*args, **kwargs)

    def get(self, request, id=None, *args, **kwargs):
        self.id_homepage = id
        return super(CampotecHomepagePreview, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CampotecHomepagePreview, self).get_context_data(**kwargs)
        context.update({
            'form': LoginForm(),
            'homepage': Homepage.objects.get(id=self.id_homepage),
            'branch_list': Branch.objects.filter(active=ACTIVE).order_by('-updated_at'),
            'programation_list': Programation.objects.filter(active=ACTIVE).order_by('date_time'),
        })
        return context


class CampotecSpecialtiesInscriptionView(TemplateView):
    """

    """
    template_name = "campotec/inscription.html";

    @method_decorator(campotec_login_required)
    def dispatch(self, *args, **kwargs):
        return super(CampotecSpecialtiesInscriptionView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CampotecSpecialtiesInscriptionView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        specialties_pk_list = request.POST.getlist('check_inscription')
        context = self.get_context_data(**kwargs)
        context.update({
            'error': '',
            'success': '',
        })

        #Remove todas as inscricoes:
        Specialty.remove_all_inscriptions_user(request.user)

        if specialties_pk_list:
            specialty_list = Specialty.objects.filter(pk__in=specialties_pk_list)
            num_specialty = len(specialty_list)
            # lista de especialidades validas para salvar no final das validações
            list_for_inscription = []
            # contador para saber em quantos turnos o usuario se inscreveu, precisa ser em 4 para passar.
            # A inscrição em um turno soma +1, se o turno for do tipo DIA_TODO (TURN_ALL_DAY), então soma +2
            valid_turno = 0

            if num_specialty >= 2:
                for specialty in specialty_list:
                    # VALIDA SE A INSCRICAO ESTA ATIVA specialty.active_inscription = True
                    # E SE o ramo da especialidade eh igual ao ramo do usuario
                    if specialty.active_inscription and specialty.branch.group in request.user.groups.all():
                        if len(specialty.inscription.all()) < specialty.num_places:
                            #Valida se tem mais de uma especialidade no mesmo turno/dia
                            if not [item for item in list_for_inscription if (item.date == specialty.date and (item.turn == specialty.turn or item.turn == Specialty.TURN_ALL_DAY))]:
                                list_for_inscription.append(specialty)
                                # Validacao do turno
                                if specialty.turn == Specialty.TURN_ALL_DAY:
                                    valid_turno += 2
                                else:
                                    valid_turno += 1
                            else:
                                # Especialidades conflitantes em turno/dia
                                context['error'] = _(u"Especialidades conflitantes em Turno/Dias.")
                                Specialty.remove_all_inscriptions_user(request.user)
                                break
                        else:
                            # sem vagas
                            context['error'] = _(u"Especialidades selecionadas não possuem mais vagas. Selecione outras.")
                            Specialty.remove_all_inscriptions_user(request.user)
                            break

                    else:
                        # nao pode se inscrever nesta especialidade
                        context['error'] = _(u"Especialidades selecionadas não são do seu Ramo. Selecione outras.")
                        Specialty.remove_all_inscriptions_user(request.user)
                        break
                # end for specialty_list
                # se não ocorreu erros inscreve o usuario nas especialidades list_for_inscription
                if valid_turno == 4 and not context['error']:
                    for specialty in list_for_inscription:
                        specialty.inscription.add(request.user)
                    context['success'] = _(u"Parabéns! Você foi inscrito com sucesso.")
                else:
                    context['error'] = _(u"Inscreva-se em epecialiades que contemplem os 4 turnos.")

            else:
                context['error'] = _(u"Selecione pelo menos 4 Especialidades.")
        context.update(self.get_context_data())
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(CampotecSpecialtiesInscriptionView, self).get_context_data(**kwargs)
        branch_list = Branch.objects.filter(active=ACTIVE, group__in=self.request.user.groups.all()).order_by('-updated_at')
        for branch in branch_list:
            branch.list_specialties = branch.get_specialties_actives_order_by_name_user(self.request.user)

        context.update({
            'branch_list': branch_list,
            'programation_list': Programation.objects.filter(active=ACTIVE).order_by('date_time'),
            'homepage': Homepage.objects.get(homepage_active=ACTIVE),
        })
        return context



#TODO: Nao utilizar - em testes
from django import forms
from django.forms import modelformset_factory
class SpecialtyInscriptionForm(forms.ModelForm):
    """
    """

    check_inscription = forms.CharField(label=_(u"Participar"), widget=forms.CheckboxInput(attrs={'class': "check-inscription"}), max_length=1, required=True)

    class Meta:
        model = Specialty
        fields = ['check_inscription',]

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(SpecialtyInscriptionForm, self).__init__(*args, **kwargs)

    def clean(self):

        num_inscriptions = len(self.instance.inscription.all())
        if num_inscriptions >= self.instance.num_places:
            raise forms.ValidationError(u"Não há vagas para esta Especialidade.")
        elif self.user:
            self.instance.inscription.add(self.user)
        return self.cleaned_data


# TODO: Nao utilizar - em testes
class CampotecInscriptionViews(FormView):
    """

    """

    model = Specialty
    form_class = None
    template_name = 'campotec/inscription_change.html'

    def get(self, request, *args, **kwargs):
        num_registers = 0
        self.queryset = Branch.objects.filter(active=ACTIVE,group__in=self.request.user.groups.all()).order_by('-updated_at')
        formset = None

        for branch in self.queryset:
            branch.list_specialties = branch.get_specialties_actives_order_by_name_user(self.request.user)
            num_registers += len(branch.list_specialties)

            SpecialtyFormSet = modelformset_factory(model=self.model, form=SpecialtyInscriptionForm, max_num=num_registers, min_num=num_registers,)
            formset = SpecialtyFormSet(queryset=branch.list_specialties)



        return self.render_to_response(self.get_context_data(formset=formset))
        #return super(CampotecInscriptionViews, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CampotecInscriptionViews, self).get_context_data(**kwargs)

        # for branch in context.get('object_list'):
        #     branch.list_specialties = branch.get_specialties_actives_order_by_name_user(self.request.user)

        context.update({
            'object_list': self.queryset,
            'programation_list': Programation.objects.filter(active=ACTIVE).order_by('date_time'),
        })
        return context


class JSONResponseMixin(object):
    """
    Classe para comunicar JSON em Ajax
    """

    @method_decorator(campotec_login_required)
    def dispatch(self, *args, **kwargs):
        return super(JSONResponseMixin, self).dispatch(*args, **kwargs)

    def render_to_response_json(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

