from xmlrpc.client import FastMarshaller
from django.db import models

# Create your models here.

class ProjectList(models.Model):
    CODE = models.CharField(max_length=255, null=False)
    PROJECT_NAME = models.CharField(max_length=255, null=False)
    PROJECT_NO = models.CharField(max_length=255, null=False)
    OLD_PROJECT_NO = models.CharField(max_length=255, null=False)
