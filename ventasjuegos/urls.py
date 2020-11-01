from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
  path('', views.index, name="home"),
  path('juegos/', views.games, name="games"),
  path('tarjeta-regalo/', views.gifcard, name="gifcard"),
  path('form/', views.form, name="form"),
  path('admin/', admin.site.urls),
]
