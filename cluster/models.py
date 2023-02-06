from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Содержание', default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')
    time_created = models.DateField(verbose_name='Время создания')
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

