# Generated by Django 4.2.7 on 2023-12-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importData', '0007_student_ahkam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/students'),
        ),
    ]
