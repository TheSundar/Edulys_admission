from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def save_data(request):
    name = request.GET.get('name')
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % name
    
    return HttpResponse(html)