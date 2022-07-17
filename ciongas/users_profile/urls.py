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
]