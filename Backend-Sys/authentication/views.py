import sys
sys.dont_write_bytecode = True
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import User, Organization
from .serializers import UserSerializer, OrganizationSerializer, UserRegistrationSerializer, OrganizationRegistrationSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView

class UserRegistrationView(APIView):
    """
    API View for user registration.
    This view does not require authentication.
    """
    permission_classes = [permissions.AllowAny]  # Allow any user to access this endpoint

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'status': 'User  registered successfully',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User instances.
    """
    queryset = User.objects.all().order_by('id') 
    serializer_class = UserSerializer

    # Allow unauthenticated access to the list of users
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]  # Allow any user to access the list
        else:
            permission_classes = [permissions.IsAuthenticated]  # Require authentication for other actions
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def enable_two_factor(self, request, pk=None):
        user = self.get_object()
        user.two_factor_enabled = True
        user.save()
        return Response({'status': 'Two-Factor Authentication enabled'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def disable_two_factor(self, request, pk=None):
        user = self.get_object()
        user.two_factor_enabled = False
        user.save()
        return Response({'status': 'Two-Factor Authentication disabled'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def update_phone_number(self, request, pk=None):
        user = self.get_object()
        phone_number = request.data.get('phone_number')
        if phone_number:
            user.phone_number = phone_number
            user.save()
            return Response({'status': 'Phone number updated'})
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def get_user_details(self, request, pk=None):
        user = self.get_object()
        return Response(UserSerializer(user).data)

class OrganizationRegistrationView(APIView):
    """
    API View for organization registration.
    This view does not require authentication.
    """
    permission_classes = [permissions.AllowAny]  # Allow any user to access this endpoint

    def post(self, request):
        serializer = OrganizationRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            organization = serializer.save()
            return Response({
                'status': 'Organization registered successfully',
                'organization': OrganizationSerializer(organization).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Organization instances.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Default permission for all actions

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def get_organization_details(self, request, pk=None):
        organization = self.get_object()
        return Response(OrganizationSerializer(organization).data)

    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def delete_organization(self, request, pk=None):
        organization = self.get_object()
        organization.delete()
        return Response({'status': 'Organization deleted'}, status=status.HTTP_204_NO_CONTENT)