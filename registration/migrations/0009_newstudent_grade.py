# Generated by Django 4.2.7 on 2024-06-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_newstudent_prize_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='grade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]