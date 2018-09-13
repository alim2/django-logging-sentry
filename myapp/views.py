from django.shortcuts import render, HttpResponse
from raven.contrib.django.raven_compat.models import client
import logging


def index(request):
    try:
        a = HttpResponse.charset.sldfl
    except Exception as ex:
        # client.captureException()
        # logging.getLogger('error').exception('here')
        pass
    return HttpResponse('hi')
