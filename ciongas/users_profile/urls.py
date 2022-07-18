from django.urls import path
from . import views
from .views import  EditProfileView, PasswordsEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/',PasswordsEditView.as_view(template_name='registration/change_password.html')),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]