# Generated by Django 2.2.13 on 2020-12-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_admissionstudent_application_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionstudent',
            name='migration_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
