from django.db import models

from cluster.mixins import Technologies, TechnologiesImg, Projects, ProjectsImg, Courses


# Create your models here.
class TechnologiesBIM(Technologies):
    owner = models.CharField(max_length=255, default='Лаборатория BIM')

    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'


class TechnologiesImgBIM(TechnologiesImg):
    owner = models.ForeignKey(to=TechnologiesBIM, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class ProjectsBIM(Projects):
    owner = models.CharField(max_length=255, default='Лаборатория BIM')

    class Meta:
        verbose_name = verbose_name_plural = 'Проекты'


class ProjectsImgBIM(ProjectsImg):
    owner = models.ForeignKey(to=ProjectsBIM, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class CoursesBIM(Courses):
    owner = models.CharField(max_length=255, default='Лаборатория BIM')

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
