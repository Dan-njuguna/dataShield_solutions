
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.text import slugify
from django.core.validators import EmailValidator

from dotenv import load_dotenv
import os
load_dotenv()
DBUSER = os.getenv("DBUSER")
DBNAME = os.getenv("DBNAME")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")

class Organization(models.Model):
    __doc__ = "Model representing an organization."
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="The name of the organization.")
    address = models.CharField(max_length=255, help_text="The address of the organization.")
    contact_person = models.CharField(max_length=255, help_text="The name of the contact person.")
    contact_email = models.CharField(max_length=255, validators=[EmailValidator()], help_text="The email address of the contact person.")
    contact_number = models.CharField(max_length=20, help_text="The contact number of the organization.")
    industry = models.CharField(max_length=255, help_text="The industry in which the organization operates.")
    company_size = models.CharField(max_length=100, help_text="The size of the company.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the organization was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the organization was last updated.")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Unique slug for the organization.")

    def save(self, *args, **kwargs):
        """Override save method to generate slug from organization name."""
        self.slug = slugify(self.name)
        (super().save)(*args, **kwargs)

    def __str__(self):
        """Return string representation of the organization."""
        return self.name


class UserManager(BaseUserManager):
    __doc__ = "Manager for the custom User model."

    def create_user(self, email, first_name, last_name, organization, password=None):
        """Create and return a user with an email, first name, last name, organization, and password."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, organization=organization)
        user.set_password(password)
        user.save(using=(self._db))
        return user

    def create_superuser(self, email, first_name, last_name, organization, password):
        """Create and return a superuser with an email, first name, last name, organization, and password."""
        user = self.create_user(email, first_name, last_name, organization, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=(self._db))
        return user


class User(AbstractBaseUser, PermissionsMixin):
    __doc__ = "Custom User model."
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, help_text="First name of the user.")
    last_name = models.CharField(max_length=255, help_text="Last name of the user.")
    email = models.EmailField(max_length=300, unique=True, help_text="Unique email address of the user.")
    organization = models.ForeignKey(Organization, on_delete=(models.CASCADE), related_name="users", help_text="The organization the user belongs to.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the user was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the user was last updated.")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Unique slug for the user.")
    is_active = models.BooleanField(default=True, help_text="Indicates if the user is active.")
    is_staff = models.BooleanField(default=False, help_text="Indicates if the user can log into the admin interface.")
    groups = models.ManyToManyField("auth.Group",
      related_name="custom_user_set",
      blank=True,
      help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.")
    user_permissions = models.ManyToManyField("auth.Permission",
      related_name="custom_user_permissions_set",
      blank=True,
      help_text="Specific permissions for this user.")
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "organization"]

    def save(self, *args, **kwargs):
        """Override save method to generate slug from email."""
        self.slug = slugify(self.email)
        (super().save)(*args, **kwargs)

    def __str__(self):
        """Return string representation of the user."""
        return self.email

    def get_full_name(self):
        """Return the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Return the short name of the user."""
        return self.first_name


