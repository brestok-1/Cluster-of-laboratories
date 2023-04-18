from PIL import Image
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заголовок новости')
    description = RichTextUploadingField(verbose_name='Содержание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')
    time_created = models.DateField(verbose_name='Время создания')
    time_updated = models.DateField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'Новость : {self.name}'

    def get_images(self):
        return NewsImg.objects.filter(news_id=self.id)

    def type(self):
        return self.__class__.__name__


class NewsImg(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    news = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name='Привязать к новости:')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Изображение {self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size
        if width / height > 4 / 3:
            new_width = int(height * 4 / 3)
            left = int((width - new_width) / 2)
            right = int(left + new_width)
            img = img.crop((left, 0, right, height))
            img.save(self.image.path)


class Students(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вопросы студентов')
    content = models.TextField(verbose_name='Ответ на вопрос', default='')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')

    class Meta:
        verbose_name = 'Студентам'
        verbose_name_plural = 'Студентам'

    def __str__(self):
        return f'Вопрос : {self.title}'
