"""tasksheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from task_sheet import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('ProjectList/',views.Project_List, name="ProjectList"),
    path('TaskSheet/ProjectList/',views.Project_List, name="ProjectList"),
    path('TaskSheet/', views.TaskSheet, name="TaskSheet"),
    path('TaskSheet/TaskSheet/', views.TaskSheet, name="TaskSheet"),
#---------------kayaroganam----------------------------
    path('TaskSheet/kayaroganam/', views.kayaroganam_task, name="kayaroganam_task"),
    path('TaskSheet/kayaroganam/add_task/', views.add_task, name="add_task"),
    path('TaskSheet/kayaroganam/add_task/addrecord/', views.adding, name="adding"),
    path('TaskSheet/kayaroganam/delete/<int:id>', views.delete, name="delete"),
    path('TaskSheet/kayaroganam/edit/<int:id>',views.edit, name="edit"),
    path('TaskSheet/kayaroganam/edit/editrecord/<int:id>',views.editrecord, name="editrecord"),
#---------------rangarajan----------------------------
    path('TaskSheet/rangarajan/', views.rangarajan_task, name="rangarajan_task"),
    path('TaskSheet/rangarajan/add_task/', views.rangarajan_add_task, name="add_task"),
    path('TaskSheet/rangarajan/add_task/addrecord/', views.rangarajan_adding, name="adding"),
    path('TaskSheet/rangarajan/delete/<int:id>', views.rangarajan_delete, name="delete"),
    path('TaskSheet/rangarajan/edit/<int:id>',views.rangarajan_edit, name="edit"),
    path('TaskSheet/rangarajan/edit/editrecord/<int:id>',views.rangarajan_editrecord, name="editrecord"),
#---------------newtest----------------------------
    path('TaskSheet/newtest/', views.newtest_task, name="newtest_task"),
    path('TaskSheet/newtest/add_task/', views.newtest_add_task, name="add_task"),
    path('TaskSheet/newtest/add_task/addrecord/', views.newtest_adding, name="adding"),
    path('TaskSheet/newtest/delete/<int:id>', views.newtest_delete, name="delete"),
    path('TaskSheet/newtest/edit/<int:id>',views.newtest_edit, name="edit"),
    path('TaskSheet/newtest/edit/editrecord/<int:id>',views.newtest_editrecord, name="editrecord"),
#---------------test----------------------------
    path('TaskSheet/test/', views.test_task, name="test_task"),
    path('TaskSheet/test/add_task/', views.test_add_task, name="add_task"),
    path('TaskSheet/test/add_task/addrecord/', views.test_adding, name="adding"),
    path('TaskSheet/test/delete/<int:id>', views.test_delete, name="delete"),
    path('TaskSheet/test/edit/<int:id>',views.test_edit, name="edit"),
    path('TaskSheet/test/edit/editrecord/<int:id>',views.test_editrecord, name="editrecord"),
]
