# Generated by Django 4.1.5 on 2023-02-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BIM', '0002_alter_projectsbim_time_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesbim',
            name='owner',
            field=models.CharField(default='Лаборатория BIM', max_length=255),
        ),
        migrations.AddField(
            model_name='projectsbim',
            name='owner',
            field=models.CharField(default='Лаборатория BIM', max_length=255),
        ),
        migrations.AddField(
            model_name='technologiesbim',
            name='owner',
            field=models.CharField(default='Лаборатория BIM', max_length=255),
        ),
    ]
