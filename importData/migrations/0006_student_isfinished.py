# Generated by Django 4.2.7 on 2023-12-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importData', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
    ]
