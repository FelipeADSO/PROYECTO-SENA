from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login as auth_login
from .forms import estrenosForm

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

def somos(request):
    return render(request, 'somos.html')

def estrenos(request):
    return render(request, 'estrenos.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "¡Registro exitoso! Has iniciado sesión.")
                return redirect('login')  # Redirige a la página principal o dashboard

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Por favor, ingresa ambos campos.')
            return render(request, 'login.html')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return render(request, 'login.html')

        if user is not None:
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                return redirect('productos')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        else:
            messages.error(request, 'El usuario no está registrado.')

    return render(request, 'login.html')


def agregar_Peliculas (request): 
    if request.method == 'POST': 
        form = estrenosForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('estrenos') # Redirige a la lista de produ 
    else: 
        form = estrenosForm() 
    return render(request, 'agrear_Peliculas.html', {'form': form})