from django.db import models

from cluster.mixins import Technologies, TechnologiesImg, Projects, ProjectsImg, Courses


# Create your models here.
class TechnologiesVision(Technologies):
    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'


class TechnologiesImgVision(TechnologiesImg):
    owner = models.ForeignKey(to=TechnologiesVision, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class ProjectsVision(Projects):
    class Meta:
        verbose_name = verbose_name_plural = 'Проект'


class ProjectsImgVision(ProjectsImg):
    owner = models.ForeignKey(to=ProjectsVision, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class CoursesVision(Courses):
    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
