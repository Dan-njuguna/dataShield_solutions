from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import User, Organization, DataProtectionRegulation, Gdpr4, KenyaDPA, ComplianceStatus
from .forms import OrganizationCreationForm, UserRegistrationForm, KenyaDPAForm, Gdpr4Form, DataProtectionRegulationForm, ComplianceStatusForm

def home(request):
    return render(request, 'test_backend_app/home.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'test_backend_app/login_register.html')

def user_register(request, organization_slug):
    organization = get_object_or_404(Organization, slug=organization_slug)
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.organization = organization
            user.set_password(user_form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        user_form = UserRegistrationForm()
    return render(request, 'test_backend_app/login_register.html', {'form': user_form, 'organization': organization})

def register_organization(request, slug):
    organization = get_object_or_404(Organization, slug=slug)
    
    if request.method == 'POST':
        org_form = OrganizationCreationForm(request.POST)
        if org_form.is_valid():
            organization = org_form.save()
            return redirect('register_user', organization_slug=organization.slug)  # Redirect to user registration with slug
    else:
        org_form = OrganizationCreationForm()
    return render(request, 'test_backend_app/organization_registration.html', {'form': org_form, 'organization': organization})



# View to list all compliance statuses
def compliance_status_list(request):
    statuses = ComplianceStatus.objects.all()
    return render(request, 'compliance_status_list.html', {'statuses': statuses})

# View to create a new compliance status
def compliance_status_create(request):
    if request.method == 'POST':
        form = ComplianceStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compliance_status_list')  # Redirect to the list view
    else:
        form = ComplianceStatusForm()
    return render(request, 'compliance_status_form.html', {'form': form})

# View to list all GDPR articles
def gdpr4_list(request):
    gdpr_articles = Gdpr4.objects.all()
    return render(request, 'gdpr4_list.html', {'gdpr_articles': gdpr_articles})

# View to create a new GDPR article
def gdpr4_create(request):
    if request.method == 'POST':
        form = Gdpr4Form(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('gdpr4_list')
    else:
        form = Gdpr4Form()
    return render(request, 'gdpr4_form.html', {'form': form})

# View to list all Kenya DPAs
def kenya_dpa_list(request):
    kenya_dpas = KenyaDPA.objects.all()
    return render(request, 'kenya_dpa_list.html', {'kenya_dpas': kenya_dpas})

# View to create a new Kenya DPA
def kenya_dpa_create(request):
    if request.method == 'POST':
        form = KenyaDPAForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('kenya_dpa_list')
    else:
        form = KenyaDPAForm()
    return render(request, 'kenya_dpa_form.html', {'form': form})

# View to list all data protection regulations
def data_protection_regulation_list(request):
    regulations = DataProtectionRegulation.objects.all()
    return render(request, 'data_protection_regulation_list.html', {'regulations': regulations})

# View to create a new data protection regulation
def data_protection_regulation_create(request):
    if request.method == 'POST':
        form = DataProtectionRegulationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('data_protection_regulation_list')
    else:
        form = DataProtectionRegulationForm()
    return render(request, 'data_protection_regulation_form.html', {'form': form})
