from django.shortcuts import render, HttpResponse
from raven.contrib.django.raven_compat.models import client


def index(request):
    client.captureException()
    return HttpResponse('hi')
