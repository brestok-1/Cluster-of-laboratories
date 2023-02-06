from django.contrib import admin

from robotics.models import TechnologiesRobotics, TechnologiesImgRobotics, ProjectsImgRobotics, ProjectsRobotics, \
    CoursesRobotics


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgRobotics
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesRobotics)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectsImgAdmin(admin.TabularInline):
    model = ProjectsImgRobotics
    fields = ('img',)
    extra = 1


@admin.register(ProjectsRobotics)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = (ProjectsImgAdmin,)
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CoursesRobotics)
class CoursesVisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'slug', 'durations', 'lector', 'course_link')
    prepopulated_fields = {'slug': ('name',)}
