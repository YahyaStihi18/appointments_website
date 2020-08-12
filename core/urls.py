from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('appointment/', views.appointment,name='appointment'),
    path('staff/', views.staff,name='satff'),
    path('staff/check_appointment/<int:id>/', views.check_appointment,name='check_appointment'),
    path('staff/change_status/<int:id>',views.change_status,name='change_status'),
    ]