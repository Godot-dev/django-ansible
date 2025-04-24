from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  

from app1.models import *


# Create your views here.
def index(request):
    context = {"personnes": Person.objects.all()}
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
        print("COMPTE CREE AVEC SUCCES !")  
    else:  
        form = UserCreationForm()  
    context['form'] = form
    return render(request, 'app1/register.html', context)  

def api_person_list(request):
    persons = Person.objects.all()
    
