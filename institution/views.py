# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse, resolve

from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class InstitutionHomepageView(TemplateView):
    """
    URL: http://g1.globo.com/dynamo/economia/rss2.xml
    """

    template_name = "institution/index.html"

    def get(self, request, *args, **kwargs):
        return super(InstitutionHomepageView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InstitutionHomepageView, self).get_context_data(**kwargs)
        return context

