from django.db import models

from cluster.mixins import Technologies, TechnologiesImg, Projects, ProjectsImg, Courses


# Create your models here.
class TechnologiesVision(Technologies):
    owner = models.CharField(max_length=255, default='Лаборатория Технического зрения')

    class Meta:
        verbose_name = verbose_name_plural = 'Технологии'

    def get_images(self):
        return TechnologiesImgVision.objects.filter(owner_id=self.id)


class TechnologiesImgVision(TechnologiesImg):
    owner = models.ForeignKey(to=TechnologiesVision, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения Технологии'


class ProjectsVision(Projects):
    owner = models.CharField(max_length=255, default='Лаборатория Технического зрения')

    class Meta:
        verbose_name = verbose_name_plural = 'Проекты'


class ProjectsImgVision(ProjectsImg):
    owner = models.ForeignKey(to=ProjectsVision, on_delete=models.CASCADE, verbose_name="Привязать изображения к")

    class Meta:
        verbose_name_plural = verbose_name = 'Изображения для технологии'


class CoursesVision(Courses):
    owner = models.CharField(max_length=255, default='Лаборатория Техического зрения')

    class Meta:
        verbose_name_plural = verbose_name = 'Курсы'
