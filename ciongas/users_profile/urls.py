from django.urls import path
from . import views
from .views import UserProfileView, EditProfileView

urlpatterns = [
    path('registration/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),

]