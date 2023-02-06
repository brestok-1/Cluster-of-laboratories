from django.contrib import admin

from technical_vision.models import TechnologiesVision, TechnologiesImgVision, ProjectsImgVision, ProjectsVision, \
    CoursesVision


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgVision
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesVision)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    prepopulated_fields = {'slug': ('name',)}


class ProjectsImgAdmin(admin.TabularInline):
    model = ProjectsImgVision
    fields = ('img',)
    extra = 1


@admin.register(ProjectsVision)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = (ProjectsImgAdmin,)
    search_fields = ('name',)
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CoursesVision)
class CoursesVisionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'slug', 'durations', 'lector', 'course_link')
    prepopulated_fields = {'slug': ('name',)}
