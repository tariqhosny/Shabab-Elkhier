# Generated by Django 4.2.7 on 2024-10-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importData', '0015_alter_grade_options_alter_year_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_grade',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]