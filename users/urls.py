from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .forms import EmailValidationOnForgotPassword


urlpatterns = [

    path('profile/', views.profile,name='profile'),
    path('profile/delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('profile/view_appointment/<int:id>/',views.view_appointment,name='view_appointment'),
    path('add_info/',views.add_info,name='add_info'),

    path('register/', views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,template_name='users/password_reset.html'),name='password_reset' ),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done' ),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm' ),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete' ),


]