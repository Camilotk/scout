# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.template import RequestContext


def error404(request):
    """
    View de Erro 404
    """
    return render_to_response('core/error404.html', RequestContext(request, {}))


def error500(request):
    """
    View de Erro 500
    """
    return render_to_response('core/error500.html', RequestContext(request, {}))
