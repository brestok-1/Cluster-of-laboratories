'''    Абстрактные классы моделей для лабораторий     '''
from django.db import models


class Technologies(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя технологии')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание технологии', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')

    class Meta:
        abstract = True

    def __str__(self):
        return f'Технология - {self.name}'

    def get_images(self):
        return TechnologiesImg.objects.filter(owner_id=self.id)


class TechnologiesImg(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        abstract = True


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание проекта', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')

    class Meta:
        abstract = True

    def __str__(self):
        return f'Проект - {self.name} {self.time_created}'

    def get_images(self):
        return ProjectsImg.objects.filter(owner_id=self.id)


class ProjectsImg(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        abstract = True


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    durations = models.IntegerField(verbose_name='Продолжительность курса (часы)')
    lector = models.CharField(max_length=255, verbose_name='Имя лектора')
    course_link = models.URLField(verbose_name="Ссылка на курс")

    class Meta:
        abstract = True

    def __str__(self):
        return f'Курс - {self.name.title()}'
