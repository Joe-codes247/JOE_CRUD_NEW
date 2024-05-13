from django.urls import path
from . import views

APP_NAME = 'market'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')


]