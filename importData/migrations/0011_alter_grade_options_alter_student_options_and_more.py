# Generated by Django 4.2.7 on 2024-04-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importData', '0010_alter_part_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['student']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='grade',
            name='fromBaqra',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='ahkam',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='next_amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='importData.part'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
