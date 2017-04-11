from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {0!s}.</body></html>".format(now)
    return HttpResponse(html)