# from django.db import models
#
#
# class Laboratory(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
#
#     def get_about_info(self):
#         return False
#
#
# class AboutLaboratory(models.Model):
#     owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name='Информация об')
#     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
#     content = models.TextField(verbose_name='Информация о лаборатории', default='')
#
#     class Meta:
#         verbose_name_plural = verbose_name = 'Об лаборатории'
#
#     def __str__(self):
#         return self.owner.name
#
#
# class AboutLaboratoryImg(models.Model):
#     owner = models.ForeignKey(to=AboutLaboratory, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
#     img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
#
#     class Meta:
#         verbose_name_plural = verbose_name = 'Изображения к страничке About'
#
#
# class Technologies(models.Model):
#     owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name="Привязать технологии к")
#     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
#     title = models.CharField(max_length=255, verbose_name='Название технологии')
#     description = models.TextField(verbose_name='Описание технологии', default='')
#     video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
#
#     class Meta:
#         verbose_name = verbose_name_plural = 'Технологии'
#
#
# class TechnologiesImg(models.Model):
#     owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
#     img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
#
#     class Meta:
#         verbose_name_plural = verbose_name = 'Изображения Технологии'
#
#
# class Projects(models.Model):
#     owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name="Привязать проект к")
#     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
#     title = models.CharField(max_length=255, verbose_name='Название проекта')
#     description = models.TextField(verbose_name='Описание проекта', default='')
#     video_link = models.CharField(max_length=1000, verbose_name='Ссылка на видео', blank=True)
#
#     class Meta:
#         verbose_name = verbose_name_plural = 'Проект'
#
#
# class ProjectsImg(models.Model):
#     owner = models.ForeignKey(to=Technologies, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
#     img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
#
#     class Meta:
#         verbose_name_plural = verbose_name = 'Изображения к страраничке About'
#
# class Courses(models.Model):
#     owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name="Привязать проект к")
#     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
#     title = models.CharField(max_length=255, verbose_name='Название проекта')
#     durations = models.IntegerField(verbose_name='Продолжительность курса (часы)')
#     lector = models.CharField(max_length=255, verbose_name='Имя лектора')
#     course_link = models.URLField(verbose_name="Ссылка на курс")
#
#     class Meta:
#         verbose_name_plural = verbose_name = 'Курсы'
#
# #
# # class Contacts(models.Model):
# #     owner = models.ForeignKey(to=Laboratory, on_delete=models.CASCADE, verbose_name="Привязать проект к")
# #     slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL', default='')
# #
# #     class Meta:
# #         verbose_name = verbose_name_plural = 'Контакты'
