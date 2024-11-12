from django.test import TestCase
from django.urls import reverse
from .models import User, Organization
from .forms import UserRegistrationForm, OrganizationRegistrationForm

class UserModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Test Org")  
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User ',
            organization=self.organization  # Provide organization
        )
        self.client.login(email='test@example.com', password='testpassword')  # Log in the user

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User ')


    def test_user_str(self):
        self.assertEqual(str(self.user), 'test@example.com')  
class OrganizationModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            name='Test Organization',
            contact_person='John Doe',
            contact_email='john@example.com',
            contact_number='1234567890',
            industry='Technology',
            company_size='Small'
        )

    def test_organization_creation(self):
        self.assertEqual(self.organization.name, 'Test Organization')
        self.assertEqual(self.organization.contact_person, 'John Doe')
        self.assertEqual(self.organization.contact_email, 'john@example.com')

    def test_organization_str(self):
        self.assertEqual(str(self.organization), 'Test Organization')  # Adjust based on your __str__ method


class UserRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User ',
            'organization': None,  # Adjust if you have an organization
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User ',
            'organization': None,
            'password': 'testpassword',
            'confirm_password': 'differentpassword'  # Passwords do not match
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match.', form.errors['__all__'])


class OrganizationRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Test Organization',
            'address': '123 Test St',
            'contact_person': 'John Doe',
            'contact_email': 'john@example.com',
            'contact_number': '1234567890',
            'industry': 'Technology',
            'company_size': 'Small',
        }
        form = OrganizationRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'name': '',
            'address': '123 Test St',
            'contact_person': 'John Doe',
            'contact_email': 'john@example.com',
            'contact_number': '1234567890',
            'industry': 'Technology',
            'company_size': 'Small',
        }
        form = OrganizationRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['name'])


class UserViewTests(TestCase):
    def test_user_registration_view(self):
        response = self.client.get(reverse('user-list'))  # Adjusted to the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/user_registration.html')  # Adjust the template name

    def test_successful_user_registration(self):
        response = self.client.post(reverse('user-list'), {  # Adjusted to the correct URL name
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User ',
            'organization': None,  # Adjust if necessary
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)  # Expecting a 201 Created status for successful registration
        self.assertTrue(User.objects.filter(email='test@example.com').exists())


class OrganizationViewTests(TestCase):
    def test_organization_registration_view(self):
        response = self.client.get(reverse('organization-list'))  # Adjusted to the correct URL name
        self.assertEqual(response.status_code,  200)
        self.assertTemplateUsed(response, 'registration/organization_registration.html')  # Adjust the template name

    def test_successful_organization_registration(self):
        response = self.client.post(reverse('organization-list'), {  # Adjusted to the correct URL name
            'name': 'Test Organization',
            'address': '123 Test St',
            'contact_person': 'John Doe',
            'contact_email': 'john@example.com',
            'contact_number': '1234567890',
            'industry': 'Technology',
            'company_size': 'Small',
        })
        self.assertEqual(response.status_code, 201)  # Expecting a 201 Created status for successful registration
        self.assertTrue(Organization.objects.filter(name='Test Organization').exists())

    def test_invalid_organization_registration(self):
        response = self.client.post(reverse('organization-list'), {  # Adjusted to the correct URL name
            'name': '',  # Invalid name
            'address': '123 Test St',
            'contact_person': 'John Doe',
            'contact_email': 'john@example.com',
            'contact_number': '1234567890',
            'industry': 'Technology',
            'company_size': 'Small',
        })
        self.assertEqual(response.status_code, 400)  # Expecting a 400 Bad Request for validation errors
        self.assertFormError(response, 'form', 'name', 'This field is required.')  # Check for form error

    def test_organization_list_view(self):
        Organization.objects.create(
            name='Test Organization',
            contact_person='John Doe',
            contact_email='john@example.com',
            contact_number='1234567890',
            industry='Technology',
            company_size='Small',
        )
        response = self.client.get(reverse('organization-list'))  # Adjusted to the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Organization')  # Check if the organization is listed

    def test_organization_detail_view(self):
        organization = Organization.objects.create(
            name='Test Organization',
            contact_person='John Doe',
            contact_email='john@example.com',
            contact_number='1234567890',
            industry='Technology',
            company_size='Small',
        )
        response = self.client.get(reverse('organization-detail', args=[organization.id]))  # Adjusted to the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Organization')  # Check if the organization details are displayed