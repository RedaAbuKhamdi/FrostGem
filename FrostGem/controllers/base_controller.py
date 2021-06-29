from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    page = loader.get_template('index.html')
    return HttpResponse(page.render())