from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
def save_data(request):
    name = request.GET.get('name')
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % name
    return HttpResponse(html)
>>>>>>> origin/Admission
