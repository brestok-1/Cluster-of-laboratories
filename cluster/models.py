from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Содержание', default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')
    time_created = models.DateField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateField(auto_now=True, verbose_name='Время обновления')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'Новость : {self.title}'

    def get_images(self):
        return NewsImg.objects.filter(news_id=self.id)


class NewsImg(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name='Привязать к новости:')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Изображение {self.id}'


class Students(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вопросы студентов')
    content = models.TextField(verbose_name='Ответ на вопрос', default='')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')

    class Meta:
        verbose_name = 'Студентам'
        verbose_name_plural = 'Студентам'

    def __str__(self):
        return f'Вопрос : {self.title}'


'''    Абстрактные классы моделей для лабораторий     '''


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
        abstract = True


class Projects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    description = models.TextField(verbose_name='Описание проекта', default='')
    video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Проект'
        abstract = True

    def __str__(self):
        return f'Проект - {self.name}'

    def get_images(self):
        return ProjectsImg.objects.filter(owner_id=self.id)


class ProjectsImg(models.Model):
    owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'
        abstract = True


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
    durations = models.IntegerField(verbose_name='Продолжительность курса (часы)')
    lector = models.CharField(max_length=255, verbose_name='Имя лектора')
    course_link = models.URLField(verbose_name="Ссылка на курс")

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
        abstract = True
