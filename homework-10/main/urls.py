
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('registration/', views.registration_view, name='registration'),
    path('programmer-day/', views.programmer_day_view, name='programmer_day'),
]
