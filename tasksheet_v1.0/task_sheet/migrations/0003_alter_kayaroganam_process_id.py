# Generated by Django 4.0.4 on 2022-05-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_sheet', '0002_kayaroganam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayaroganam',
            name='process_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
