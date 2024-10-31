from django.http import JsonResponse, Http404
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import User, Organization
from .forms import UserRegistrationForm, OrganizationRegistrationForm
import json

@csrf_exempt
def user_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'success':True,  'user_id':user.id,  'slug':user.slug}, status=201)
        return JsonResponse({'success':False,  'errors':form.errors}, status=400)
    return JsonResponse({'success':False,  'message':"Invalid request method."}, status=400)


@csrf_exempt
def organization_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = OrganizationRegistrationForm(data)
        if form.is_valid():
            organization = form.save()
            return JsonResponse({'success':True,  'organization_id':organization.id,  'slug':organization.slug}, status=201)
        return JsonResponse({'success':False,  'errors':form.errors}, status=400)
    return JsonResponse({'success':False,  'message':"Invalid request method."}, status=400)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success':True,  'user_id':user.id}, status=200)
        return JsonResponse({'success':False,  'message':"Invalid credentials."}, status=400)
    return JsonResponse({'success':False,  'message':"Invalid request method."}, status=400)


def user_list(request):
    users = User.objects.all()
    return JsonResponse({"users": (list(users.values()))}, safe=False)


def organization_list(request):
    organizations = Organization.objects.all()
    return JsonResponse({"organizations": (list(organizations.values()))}, safe=False)


def user_detail(request, slug):
    try:
        user = User.objects.get(slug=slug)
        user_data = {'id':user.id, 
         'first_name':user.first_name, 
         'last_name':user.last_name, 
         'email':user.email, 
         'organization':(user.organization).name, 
         'slug':user.slug}
        return JsonResponse({"user": user_data}, status=200)
    except User.DoesNotExist:
        raise Http404("User  not found")


def organization_detail(request, slug):
    try:
        organization = Organization.objects.get(slug=slug)
        organization_data = {'id':organization.id, 
         'name':organization.name, 
         'contact_person':organization.contact_person, 
         'contact_email':organization.contact_email, 
         'contact_number':organization.contact_number, 
         'industry':organization.industry, 
         'company_size':organization.company_size, 
         'slug':organization.slug}
        return JsonResponse({"organization": organization_data}, status=200)
    except Organization.DoesNotExist:
        raise Http404("Organization not found")

# okay decompiling views.cpython-38.pyc
