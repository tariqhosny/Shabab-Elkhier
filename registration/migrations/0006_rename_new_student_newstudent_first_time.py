# Generated by Django 4.2.7 on 2024-05-03 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_rename_newstudent_newstudent_new_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstudent',
            old_name='new_student',
            new_name='first_time',
        ),
    ]
