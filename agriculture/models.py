from django.db import models

from cluster.mixins import Technologies, TechnologiesImg, Projects, ProjectsImg, Courses


# Create your models here.
class TechnologiesAgriculture(Technologies):
    owner = models.CharField(max_length=255, default='Лаборатория Точного земледелия')

    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'


class TechnologiesImgAgriculture(TechnologiesImg):
    owner = models.ForeignKey(to=TechnologiesAgriculture, on_delete=models.CASCADE,
                              verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class ProjectsAgriculture(Projects):
    owner = models.CharField(max_length=255, default='Лаборатория Точного земледелия')

    class Meta:
        verbose_name = verbose_name_plural = 'Проекты'


class ProjectsImgAgriculture(ProjectsImg):
    owner = models.ForeignKey(to=ProjectsAgriculture, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class CoursesAgriculture(Courses):
    owner = models.CharField(max_length=255, default='Лаборатория Точного земледелия')

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
