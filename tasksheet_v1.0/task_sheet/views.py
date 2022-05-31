from re import template
from defer import return_value
from django.shortcuts import render
from .models import ProjectList
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.urls import reverse

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


#-------------------kayaroganam-------------------------------
def kayaroganam_task(request):
    task_sheet = kayaroganam.objects.all().values()
    template = loader.get_template('show_Task_Sheet.html')
    context = {
        'task_sheet' : task_sheet
    }
    return HttpResponse(template.render(context, request))

def add_task(request):
    return render(request, 'add.html')

def adding(request):
    a = request.POST['serial_no']
    b = request.POST['project_no']
    c = request.POST['project_name']
    d = request.POST['process_id']
    e = request.POST['process_sequence']
    f = request.POST['estimated_hours']
    g = request.POST['tasks']
    h = request.POST['server_link']
    i = request.POST['date']
    j = request.POST['hours']
    task = kayaroganam(s_no=a, project_no=b, project_name=c, process_id=d, process_sequence=e, estimated_hours=f, tasks=g, server_link=h, date=i, hours=j)
    task.save()
    return HttpResponseRedirect(reverse('kayaroganam_task'))

def delete(request, id):
    task = kayaroganam.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('kayaroganam_task'))

def edit(request, id):
    task = kayaroganam.objects.get(id=id)
    template = loader.get_template("edit.html")
    context = {
        'task':task
    }
    return HttpResponse(template.render(context, request))

def editrecord(request, id):
    task = kayaroganam.objects.get(id=id)
    a = request.POST['serial_no']
    b = request.POST['project_no']
    c = request.POST['project_name']
    d = request.POST['process_id']
    e = request.POST['process_sequence']
    f = request.POST['estimated_hours']
    g = request.POST['tasks']
    h = request.POST['server_link']
    i = request.POST['date']
    j = request.POST['hours']
    task.s_no = a
    task.project_no = b
    task.project_name = c
    task.process_id = d
    task.process_sequence = e
    task.estimated_hours = f
    task.tasks = g
    task.server_link = h
    task.date = i
    task.hours = j
    task.save()
    return HttpResponseRedirect(reverse('kayaroganam_task'))

#-------------------rangarajan-------------------------------

def rangarajan_task(request):
    task_sheet = rangarajan.objects.all().values()
    template = loader.get_template('show_Task_Sheet.html')
    context = {
        'task_sheet' : task_sheet
    }
    return HttpResponse(template.render(context, request))

def rangarajan_add_task(request):
    return render(request, 'add.html')

def rangarajan_adding(request):
    a = request.POST['serial_no']
    b = request.POST['project_no']
    c = request.POST['project_name']
    d = request.POST['process_id']
    e = request.POST['process_sequence']
    f = request.POST['estimated_hours']
    g = request.POST['tasks']
    h = request.POST['server_link']
    i = request.POST['date']
    j = request.POST['hours']
    task = rangarajan(s_no=a, project_no=b, project_name=c, process_id=d, process_sequence=e, estimated_hours=f, tasks=g, server_link=h, date=i, hours=j)
    task.save()
    return HttpResponseRedirect(reverse('rangarajan_task'))

def rangarajan_delete(request, id):
    task = rangarajan.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('rangarajan_task'))

def rangarajan_edit(request, id):
    task = rangarajan.objects.get(id=id)
    template = loader.get_template("edit.html")
    context = {
        'task':task
    }
    return HttpResponse(template.render(context, request))

def rangarajan_editrecord(request, id):
    task = rangarajan.objects.get(id=id)
    a = request.POST['serial_no']
    b = request.POST['project_no']
    c = request.POST['project_name']
    d = request.POST['process_id']
    e = request.POST['process_sequence']
    f = request.POST['estimated_hours']
    g = request.POST['tasks']
    h = request.POST['server_link']
    i = request.POST['date']
    j = request.POST['hours']
    task.s_no = a
    task.project_no = b
    task.project_name = c
    task.process_id = d
    task.process_sequence = e
    task.estimated_hours = f
    task.tasks = g
    task.server_link = h
    task.date = i
    task.hours = j
    task.save()
    return HttpResponseRedirect(reverse('rangarajan_task'))
