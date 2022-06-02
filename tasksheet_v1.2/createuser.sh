#!/bin/bash


read -p "User Name: " USER_NAME


#__________models.py___________

echo "" >> ./task_sheet/models.py
echo "#-----------${USER_NAME}--------------" >> task_sheet/models.py
echo "class ${USER_NAME}(models.Model):
    s_no = models.IntegerField()
    project_no = models.CharField(max_length=255, null=False)
    project_name = models.CharField(max_length=255, null=False)
    process_id = models.CharField(max_length=255, null=True)
    process_sequence = models.CharField(max_length=255)
    estimated_hours = models.FloatField(max_length=255, null=False)
    tasks = models.CharField(max_length=255)
    server_link = models.CharField(max_length=255, null=True)
    date = models.DateField()
    hours = models.FloatField()" >> task_sheet/models.py

python3 manage.py makemigrations
python3 manage.py migrate

#__________admin.py___________

echo "" >> task_sheet/admin.py
echo "#-----------${USER_NAME}--------------" >> task_sheet/admin.py
echo "admin.site.register(${USER_NAME})" >> task_sheet/admin.py

#__________views.py___________

echo "" >> task_sheet/views.py
echo "#-----------${USER_NAME}--------------" >> task_sheet/views.py

echo "def ${USER_NAME}_task(request):
    task_sheet = ${USER_NAME}.objects.all().values()
    template = loader.get_template('show_Task_Sheet.html')
    context = {
        'task_sheet' : task_sheet
    }
    return HttpResponse(template.render(context, request))

def ${USER_NAME}_add_task(request):
    return render(request, 'add.html')

def ${USER_NAME}_adding(request):
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
    task = ${USER_NAME}(s_no=a, project_no=b, project_name=c, process_id=d, process_sequence=e, estimated_hours=f, tasks=g, server_link=h, date=i, hours=j)
    task.save()
    return HttpResponseRedirect(reverse('${USER_NAME}_task'))

def ${USER_NAME}_delete(request, id):
    task = ${USER_NAME}.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('${USER_NAME}_task'))

def ${USER_NAME}_edit(request, id):
    task = ${USER_NAME}.objects.get(id=id)
    template = loader.get_template(\"edit.html\")
    context = {
        'task':task
    }
    return HttpResponse(template.render(context, request))

def ${USER_NAME}_editrecord(request, id):
    task = ${USER_NAME}.objects.get(id=id)
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
    return HttpResponseRedirect(reverse('${USER_NAME}_task'))" >> task_sheet/views.py

#__________urls.py___________

sed -i '$d' tasksheet/urls.py
echo "" >> tasksheet/urls.py
echo "#---------------${USER_NAME}----------------------------
    path('TaskSheet/${USER_NAME}/', views.${USER_NAME}_task, name=\"${USER_NAME}_task\"),
    path('TaskSheet/${USER_NAME}/add_task/', views.${USER_NAME}_add_task, name=\"add_task\"),
    path('TaskSheet/${USER_NAME}/add_task/addrecord/', views.${USER_NAME}_adding, name=\"adding\"),
    path('TaskSheet/${USER_NAME}/delete/<int:id>', views.${USER_NAME}_delete, name=\"delete\"),
    path('TaskSheet/${USER_NAME}/edit/<int:id>',views.${USER_NAME}_edit, name=\"edit\"),
    path('TaskSheet/${USER_NAME}/edit/editrecord/<int:id>',views.${USER_NAME}_editrecord, name=\"editrecord\"),
]" >> tasksheet/urls.py

#__________task_sheet.html___________

sed -i '$d' templates/tasksheet.html
sed -i '$d' templates/tasksheet.html
echo "  <a href=\"${USER_NAME}/\">${USER_NAME}</a><br>
</body>
</html>" >> templates/tasksheet.html
