# Generated by Django 4.2.7 on 2024-05-03 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_newstudent_newstudent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstudent',
            old_name='newStudent',
            new_name='new_student',
        ),
    ]