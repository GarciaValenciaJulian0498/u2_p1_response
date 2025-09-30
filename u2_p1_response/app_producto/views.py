from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Hola Mundo</h1>')