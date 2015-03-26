# -*- coding:utf-8 -*-
import urlparse
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, user_logged_out
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.utils.translation import ugettext_lazy as _


def campotec_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/campotec/login'):
    """
    Sobrescreve o metodo que exige login para acessar a view
    Usar com decorator sobre o metodo que desejar o login:
    @method_decorator(campotec_login_required)
    """
    return login_required(function, redirect_field_name, login_url)


def campotec_permission_required(perm, login_url='/admin/login', raise_exception=False):
    """
    Sobrescreve o metodo que exige login para acessar a view
    Usar com decorator sobre o metodo que desejar o login:
    @method_decorator(campotec_login_required)
    """
    return permission_required(perm, login_url=login_url, raise_exception=raise_exception)


class LoginForm(AuthenticationForm):
    """
    Personalizações no formulario de Login dos usuários
    """

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = _(u"Nº Registro UEB")


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='campotec/login.html', redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=LoginForm,
          current_app=None, extra_context=None):
    """
    Realiza Login do usuário do app Campotec
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]

            # Use default setting if redirect_to is empty
            if not redirect_to:
                # redirect_to = settings.LOGIN_REDIRECT_URL
                redirect_to = reverse('campotec-inscription')

            # Heavier security check -- don't allow redirection to a different
            # host.
            elif netloc and netloc != request.get_host():
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)
    request.session.set_test_cookie()
    current_site = get_current_site(request)
    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context, current_app=current_app)


def logout(request):
    """
    Realiza Logout do usuário do App Campotec
    """
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser

        request.user = AnonymousUser()
    return redirect('campotec-homepage')
