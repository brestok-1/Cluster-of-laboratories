from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Содержание', default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')
    time_created = models.DateField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'Новость : {self.title}'


class NewsImg(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name='Привязать к новости:')


class NewsVideo(models.Model):
    video_link = models.URLField(verbose_name='Ссылка на видео')
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, blank=True, verbose_name='Привязать к новости:')
