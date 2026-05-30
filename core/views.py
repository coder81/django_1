from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', status=200)
def about(request):
    return HttpResponse("Shit heapens.", status=500)
def product(request, name):
    return HttpResponse(f'Ovo je {name}')

def user(request, userId):
    return HttpResponse(f'Ovo je korisnicki id: {userId}')