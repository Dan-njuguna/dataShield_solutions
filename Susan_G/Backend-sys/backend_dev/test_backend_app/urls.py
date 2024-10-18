from django.urls import path
from .views import home, user_login, user_register, register_organization

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/<slug:organization_slug>/', user_register, name='register_user'),
    path('register-organization/<slug:slug>/', register_organization, name='register_organization'),
]