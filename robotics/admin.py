from django.contrib import admin

from robotics.models import *


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImg
    fields = ('img',)
    extra = 1


@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectsImgAdmin(admin.TabularInline):
    model = ProjectsImg
    fields = ('img',)
    extra = 1


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = (ProjectsImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# @admin.register(Laboratory)
# class Laboratory(admin.ModelAdmin):
#     fields = ('name',)
