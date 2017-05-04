# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django_facebook.api import require_facebook_graph

def index(request):
    context = {
        'testname': "no name yet",
    }
    return HttpResponse(render(request, 'fbconn/index.html', context))

def list(request):
    #print request.GET.get('code')
    #code = request.data["code"]
    #redirect = request.data["redirectUri"]

    #user_token = FacebookAuthorization.convert_code(code=code, redirect_uri=redirect)
    #facebook = OpenFacebook(user_token['access_token'])
    facebook = require_facebook_graph(request)


    context = {
        'testname': facebook.me(),
    }

    return HttpResponse(render(request, 'fbconn/index.html', context))
