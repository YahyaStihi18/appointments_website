from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('appointment/', views.appointment,name='appointment'),
    path('staff/', views.staff,name='satff')
    ]