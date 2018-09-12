import logging
from django.shortcuts import render, HttpResponse


def index(request):
    logging.getLogger('logger_name').error("it's error")
    return HttpResponse('hi')
