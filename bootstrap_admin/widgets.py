# -*- coding:utf-8 -*-
from copy import deepcopy
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Input, Widget
from django.forms.util import flatatt


class LinkButton(Widget):
    """
    Monta um link do tipo button do bootstrap
    """

    def __init__(self, label='', href='', attrs=None):
        self.label = label
        self.href = href
        super(LinkButton, self).__init__(attrs)

    def render(self, name='', label="", href='', attrs=None):
        attrs = self.build_attrs(attrs)
        if not label:
            label = self.label
        if not href:
            href = self.href
        if not attrs.has_key('class'):
            attrs['class'] = "btn btn-info"
        if not attrs.has_key('title'):
            attrs['title'] = label

        html = u"""
            <a href="{href}" id="id_{name}" {final_attrs}>{label}</a>
            """.format(name=name, href=href, label=label, final_attrs=flatatt(self.build_attrs(attrs)))
        return mark_safe(html)
