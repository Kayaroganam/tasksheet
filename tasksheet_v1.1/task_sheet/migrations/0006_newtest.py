# Generated by Django 4.0.4 on 2022-06-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_sheet', '0005_rangarajan'),
    ]

    operations = [
        migrations.CreateModel(
            name='newtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('project_no', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('process_id', models.CharField(max_length=255, null=True)),
                ('process_sequence', models.CharField(max_length=255)),
                ('estimated_hours', models.FloatField(max_length=255)),
                ('tasks', models.CharField(max_length=255)),
                ('server_link', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('hours', models.FloatField()),
            ],
        ),
    ]