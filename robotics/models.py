from django.db import models


# Create your models here.
class Technologies(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя технологии')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание технологии', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'
        abstract = True

    def __str__(self):
        return f'Технология - {self.name}'

    def get_images(self):
        return TechnologiesImg.objects.filter(owner_id=self.id)


class TechnologiesImg(models.Model):
    owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание проекта', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Проект'

    def __str__(self):
        return f'Проект - {self.name}'

    def get_images(self):
        return ProjectsImg.objects.filter(owner_id=self.id)


class ProjectsImg(models.Model):
    owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    durations = models.IntegerField(verbose_name='Продолжительность курса (часы)')
    lector = models.CharField(max_length=255, verbose_name='Имя лектора')
    course_link = models.URLField(verbose_name="Ссылка на курс")

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
