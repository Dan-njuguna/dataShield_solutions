from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrganizationViewSet, UserRegistrationView, OrganizationRegistrationView
from rest_framework.authtoken.views import obtain_auth_token  # Import the token view

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'organizations', OrganizationViewSet, basename='organization')

urlpatterns = [
    path('register/user/', UserRegistrationView.as_view(), name='user-registration'),  # User registration endpoint
    path('register/organization/', OrganizationRegistrationView.as_view(), name='organization-registration'),  # Organization registration endpoint
    path('login/', obtain_auth_token, name='api_token_auth'),  # Token login endpoint
    path('', include(router.urls)),  # Include the router URLs
]