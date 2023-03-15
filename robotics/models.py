'''    Абстрактные классы моделей для лабораторий     '''
from django.db import models


class Laboratory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Technologies(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя технологии')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание технологии', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Технология - {self.name}'

    def get_images(self):
        return TechnologiesImg.objects.filter(owner_id=self.id)

    def type(self):
        return self.owner.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = "Технологии"


class TechnologiesImg(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE)


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание проекта', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
    time_created = models.DateField(verbose_name='Время создания')
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Проект - {self.name} {self.time_created}'

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
    durations = models.IntegerField(verbose_name='Продолжительность курса (часы)')
    lector = models.CharField(max_length=255, verbose_name='Имя лектора')
    description = models.TextField(verbose_name='Описание курса', default='')
    course_link = models.URLField(verbose_name="Ссылка на курс")
    owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Относится к')

    def __str__(self):
        return f'Курс - {self.name.title()}'

    def type(self):
        return self.__class__.__name__

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = "Курсы"
