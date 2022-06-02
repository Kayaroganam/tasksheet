from re import template
from defer import return_value
from django.shortcuts import render
from .models import ProjectList
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.urls import reverse
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Project_List(request):
    proj_list = ProjectList.objects.all().values()
    template = loader.get_template('ProjectList.html')
    context = {
        'proj_list' : proj_list
    }
    return HttpResponse(template.render(context, request))

def TaskSheet(request):
    return render(request, 'tasksheet.html')

