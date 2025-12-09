from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('fastfood/', views.fastfood_view, name='fastfood'),
    path('test/', views.test_view, name='test'),
]