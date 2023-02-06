from django.contrib import admin

from agriculture.models import TechnologiesAgriculture, TechnologiesImgAgriculture, ProjectsImgAgriculture, \
    ProjectsAgriculture, \
    CoursesAgriculture


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgAgriculture
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesAgriculture)
class TechnologiesAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectsImgAdmin(admin.TabularInline):
    model = ProjectsImgAgriculture
    fields = ('img',)
    extra = 1


@admin.register(ProjectsAgriculture)
class ProjectsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    inlines = (ProjectsImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CoursesAgriculture)
class CoursesAgricultureAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'slug', 'durations', 'lector', 'course_link')
    prepopulated_fields = {'slug': ('name',)}
