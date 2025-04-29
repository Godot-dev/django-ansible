from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from app1.models import *
from app1.serializers import *


# Create your views here.
def index(request):
    context = {"persons": Person.objects.all()}
    print(context)
    return render(request, 'app1/index.html', context)

def submit_form(request):
    p = Person.objects.create(name=request.POST.get('name'), age=request.POST.get('age'))
    p.save()
    return redirect("/")

  
def register(request):  
    context = {}
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            context['message'] = "Account created successfully"
        else:
            context['message'] = "Error ! The account has not been created"
    else:
        form = UserCreationForm()  
    context['form'] = form
    return render(request, 'app1/register.html', context)  



class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@require_POST
def user_login(request):
    body = json.loads(request.body)
    username = body.get('username')
    password = body.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        resp = login(request, user)
        print(user)
        print(resp)
        # Redirect to a success page.
        return JsonResponse({"status": "success"})
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({"status": "failed"})

@require_POST
@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({"status": "success"})

@login_required
def current_user(request):
    user = request.user
    if user.is_authenticated:
        return JsonResponse({'username': user.username})
    else:
        return JsonResponse({'username': None})
@ensure_csrf_cookie
def set_csrf_cookie(request):
    return JsonResponse({'message': 'CSRF cookie set'})