# Generated by Django 4.2.7 on 2024-04-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importData', '0012_rename_frombaqra_grade_from_baqra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='part',
            name='soura',
            field=models.ManyToManyField(to='importData.soura'),
        ),
    ]
