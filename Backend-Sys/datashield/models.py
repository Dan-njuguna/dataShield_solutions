from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin
from django.utils.text import slugify
from dotenv import  load_dotenv
import os

load_dotenv()

DBUSER = os.getenv("DBUSER")
DBNAME = os.getenv("DBNAME")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")

class Organization(models.Model):
    """Model representing an organization."""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    industry = models.CharField(max_length=255)
    company_size = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """Manager for custom User model."""
    
    def create_user(self, email, first_name, last_name, organization, password=None):
        """Create and return a user with an email, first name, last name, organization, and password."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, organization=organization)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, organization, password):
        """Create and return a superuser with an email, first name, last name, organization, and password."""
        user = self.create_user(email, first_name, last_name, organization, password)
        user.is_staff = True  # Mark as staff for admin access
        user.is_superuser = True  # Mark as superuser for full permissions
        user.save(using=self._db)
        return user


class User(AbstractBaseUser , PermissionsMixin):
    """Custom User model."""
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=300, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Indicates if the user is active
    is_staff = models.BooleanField(default=False)  # Indicates if the user can log into admin
    password = models.CharField(max_length=255, blank=True, default='')
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # Add groups and user_permissions with unique related names
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'organization']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class DataProtectionRegulation(models.Model):
    name = models.CharField(max_length=255)
    jurisdiction = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Gdpr4(models.Model):
    category = models.TextField()
    description = models.TextField()
    gdpr_articles = models.TextField()
    recitals = models.TextField()
    data_protection_regulation = models.ForeignKey(DataProtectionRegulation, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class KenyaDPA(models.Model):
    data_protection_regulation = models.ForeignKey(DataProtectionRegulation, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    section_in_act = models.CharField(max_length=50)
    key_points = models.TextField(blank=True)

    def __str__(self):
        return self.category

class ComplianceStatus(models.Model):
    COMPLIANCE_STATUS_CHOICES = [
        ('compliant', 'Compliant'),
        ('non-compliant', 'Non-Compliant'),
    ]

    compliance_status = models.CharField(max_length=20, choices=COMPLIANCE_STATUS_CHOICES)
    last_checked_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)  # Assuming Organization exists
    data_protection_regulations = models.ForeignKey(DataProtectionRegulation, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.compliance_status

class ComplianceStatusTracking(models.Model):
    compliance_status = models.ForeignKey(ComplianceStatus, on_delete=models.CASCADE)
    previous_compliance_status = models.CharField(max_length=20, blank=True)
    new_compliance_status = models.CharField(max_length=20)
    changed_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True)
    data_protection_regulations = models.ForeignKey(DataProtectionRegulation, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.new_compliance_status} - {self.changed_at}"
