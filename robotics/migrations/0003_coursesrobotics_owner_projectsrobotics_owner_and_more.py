# Generated by Django 4.1.5 on 2023-02-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotics', '0002_alter_projectsrobotics_time_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesrobotics',
            name='owner',
            field=models.CharField(default='Лаборатория Промышленной электроники', max_length=255),
        ),
        migrations.AddField(
            model_name='projectsrobotics',
            name='owner',
            field=models.CharField(default='Лаборатория Промышленной электроники', max_length=255),
        ),
        migrations.AddField(
            model_name='technologiesrobotics',
            name='owner',
            field=models.CharField(default='Лаборатория Промышленной электроники', max_length=255),
        ),
    ]
