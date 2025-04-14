from django.shortcuts import render, redirect
from app1.models import *


# Create your views here.
def index(request):
    context = {"personnes": Person.objects.all()}
    return render(request, 'app1/index.html', context)

def submit_form(request):
    p = Person.objects.create(name=request.POST.get('name'), age=request.POST.get('age'))
    p.save()
    return redirect("/")
