from rest_framework import serializers
from .models import User, Organization

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'organization', 
            'is_active', 
            'dark_mode', 
            'two_factor_enabled', 
            'phone_number', 
            'profile_picture', 
            'bio', 
            'created_at', 
            'updated_at', 
            'is_staff'
        ]
        read_only_fields = ('created_at', 'updated_at', 'is_staff')

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'organization', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            organization=validated_data.get('organization')  # Use .get to avoid KeyError
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id', 
            'name', 
            'contact_person', 
            'contact_email', 
            'contact_number', 
            'industry', 
            'company_size', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at')

class OrganizationRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'name', 
            'contact_person', 
            'contact_email', 
            'contact_number', 
            'industry', 
            'company_size'
        ]

    def validate_contact_email(self, value):
        """
        Validate that the contact email is in a valid format.
        """
        if not value.endswith('@example.com'):  # Example validation
            raise serializers.ValidationError("Contact email must be from example.com")
        return value

    def create(self, validated_data):
        organization = Organization(**validated_data)
        organization.save()
        return organization