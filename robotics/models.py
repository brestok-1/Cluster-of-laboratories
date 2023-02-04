from django.db import models

from cluster.mixins import Technologies, TechnologiesImg, Projects, ProjectsImg, Courses


# Create your models here.
class TechnologiesRobotics(Technologies):
    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'


class TechnologiesImgRobotics(TechnologiesImg):
    owner = models.ForeignKey(to=TechnologiesRobotics, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class ProjectsRobotics(Projects):
    class Meta:
        verbose_name = verbose_name_plural = 'Проект'


class ProjectsImgRobotics(ProjectsImg):
    owner = models.ForeignKey(to=ProjectsRobotics, on_delete=models.CASCADE, verbose_name="Привязать изображения к")
    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class CoursesRobotics(Courses):

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
