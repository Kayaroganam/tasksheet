from xmlrpc.client import FastMarshaller
from django.db import models

# Create your models here.

class ProjectList(models.Model):
    CODE = models.CharField(max_length=255, null=False)
    PROJECT_NAME = models.CharField(max_length=255, null=False)
    PROJECT_NO = models.CharField(max_length=255, null=False)
    OLD_PROJECT_NO = models.CharField(max_length=255, null=False)

#-----------------------kayaroganam---------------------------

class kayaroganam(models.Model):
    s_no = models.IntegerField()
    project_no = models.CharField(max_length=255, null=False)
    project_name = models.CharField(max_length=255, null=False)
    process_id = models.CharField(max_length=255, null=True)
    process_sequence = models.CharField(max_length=255)
    estimated_hours = models.FloatField(max_length=255, null=False)
    tasks = models.CharField(max_length=255)
    server_link = models.CharField(max_length=255, null=True)
    date = models.DateField()
    hours = models.FloatField()

#-----------------------rangarajan---------------------------

class rangarajan(models.Model):
    s_no = models.IntegerField()
    project_no = models.CharField(max_length=255, null=False)
    project_name = models.CharField(max_length=255, null=False)
    process_id = models.CharField(max_length=255, null=True)
    process_sequence = models.CharField(max_length=255)
    estimated_hours = models.FloatField(max_length=255, null=False)
    tasks = models.CharField(max_length=255)
    server_link = models.CharField(max_length=255, null=True)
    date = models.DateField()
    hours = models.FloatField()
