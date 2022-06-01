#!/bin/bash

read -p "User Name: " UserName

#==========models.py===========
echo "" >> task_sheet/models.py
echo "#-----------------------$UserName---------------------------

class ${UserName}(models.Model):
    s_no = models.IntegerField()
    project_no = models.CharField(max_length=255, null=False)
    project_name = models.CharField(max_length=255, null=False)
    process_id = models.CharField(max_length=255, null=True)
    process_sequence = models.CharField(max_length=255)
    estimated_hours = models.FloatField(max_length=255, null=False)
    tasks = models.CharField(max_length=255)
    server_link = models.CharField(max_length=255, null=True)
    date = models.DateField()
    hours = models.FloatField()" >> ./task_sheet/models.py

#python3 ./manage.py makemigrations
#python3 ./manage.py migrate

#==========admin.py===========
echo "" >> task_sheet/admin.py
echo "admin.site.register(${UserName})" >> ./task_sheet/admin.py

#==========urls.py===========


sed -i '$d' tasksheet/urls.py

echo "#---------------$UserName----------------------------
    path('TaskSheet/$UserName/', views.${UserName}_task, name=\"${UserName}_task\"),
    path('TaskSheet/$UserName/add_task/', views.${UserName}_add_task, name=\"add_task\"),
    path('TaskSheet/$UserName/add_task/addrecord/', views.${UserName}_adding, name=\"adding\"),
    path('TaskSheet/$UserName/delete/<int:id>', views.${UserName}_delete, name=\"delete\"),
    path('TaskSheet/$UserName/edit/<int:id>',views.${UserName}_edit, name=\"edit\"),
    path('TaskSheet/$UserName/edit/editrecord/<int:id>',views.${UserName}_editrecord, name=\"editrecord\"),
]" >> tasksheet/urls.py

#==========views.py===========
echo "" >> task_sheet/views.py

echo "#-------------------${UserName}-------------------------------

def ${UserName}_task(request):
    task_sheet = ${UserName}.objects.all().values()
    template = loader.get_template('show_Task_Sheet.html')
    context = {
        'task_sheet' : task_sheet
    }
    return HttpResponse(template.render(context, request))

def ${UserName}_add_task(request):
    return render(request, 'add.html')

def ${UserName}_adding(request):
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
    task = ${UserName}(s_no=a, project_no=b, project_name=c, process_id=d, process_sequence=e, estimated_hours=f, tasks=g, server_link=h, date=i, hours=j)
    task.save()
    return HttpResponseRedirect(reverse('${UserName}_task'))

def ${UserName}_delete(request, id):
    task = ${UserName}.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('${UserName}_task'))

def ${UserName}_edit(request, id):
    task = ${UserName}.get_template(\"edit.html\")
    context = {
        'task':task
    }
    return HttpResponse(template.render(context, request))

def ${UserName}_editrecord(request, id):
    task = ${UserName}.objects.get(id=id)
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
    return HttpResponseRedirect(reverse('${UserName}_task'))" >> task_sheet/views.py

#==========tasksheet.html===========

sed -i '$d' templates/tasksheet.html
sed -i '$d' templates/tasksheet.html
sed -i '$d' templates/tasksheet.html

echo "	<a href="${UserName}">${UserName}</a><br>
    <br><a href=\"create_new/\">create new task sheet</a>
</body>
</html>" >> templates/tasksheet.html