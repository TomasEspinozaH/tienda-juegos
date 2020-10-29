from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'core/index.html')

def games(request):
  return render(request, 'core/juegos.html')

def gifcard(request):
  return render(request, 'core/tarjeta_regalo.html')

def base(request):
  return render(request, 'core/base.html')

def form(request):
  return render(request, 'core/formulario.html')