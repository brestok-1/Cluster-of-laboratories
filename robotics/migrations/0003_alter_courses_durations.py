# Generated by Django 4.1.7 on 2023-03-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotics', '0002_alter_courses_durations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='durations',
            field=models.DurationField(verbose_name='Продолжительность курса (часы)'),
        ),
    ]