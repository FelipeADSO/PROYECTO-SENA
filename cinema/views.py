from django.shortcuts import render


# Create your views here.
 
def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def cartelera(request):
    return render(request, 'cartelera.html')

def peliculas(request):
    return render(request, 'peliculas.html')

def peliculas2(request):
    return render(request, 'peliculas2.html')

def contactenos(request):
    return render(request, 'contactenos.html')

def login(request):
    return render(request, 'login.html')

