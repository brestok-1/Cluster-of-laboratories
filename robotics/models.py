'''    Абстрактные классы моделей для лабораторий     '''
import uuid

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Laboratory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, default='')

    def __str__(self):
        return self.name


class Technologies(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя технологии')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = RichTextUploadingField(verbose_name='Описание технологии')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Технология - {self.name}'

    def get_images(self):
        return TechnologiesImg.objects.filter(owner_id=self.id)

    def type(self):
        return self.__class__.__name__

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = "Технологии"


class TechnologiesImg(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE)


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = RichTextUploadingField(verbose_name='Описание проекта')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Проект - {self.name}'

    def type(self):
        return self.__class__.__name__

    def get_images(self):
        return ProjectsImg.objects.filter(owner_id=self.id)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectsImg(models.Model):
    owner = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    durations = models.DurationField(verbose_name='Продолжительность курса')
    lector = models.CharField(max_length=255, verbose_name='Имя лектора')
    description = RichTextUploadingField(verbose_name='Описание курса')
    course_link = models.URLField(verbose_name="Ссылка на курс", blank=True)
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Курс - {self.name.title()}'

    def type(self):
        return self.__class__.__name__

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = "Курсы"
