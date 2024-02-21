from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME 2')

def contact(request):
    return HttpResponse('contact')

def about(request):
    return HttpResponse('about')