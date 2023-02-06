from django.contrib import admin

from BIM.models import TechnologiesBIM, TechnologiesImgBIM, ProjectsImgBIM, ProjectsBIM, \
    CoursesBIM


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgBIM
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesBIM)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectsImgAdmin(admin.TabularInline):
    model = ProjectsImgBIM
    fields = ('img',)
    extra = 1


@admin.register(ProjectsBIM)
class ProjectsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'video_link', 'time_created')
    inlines = (ProjectsImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CoursesBIM)
class CoursesBIMAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'slug', 'durations', 'lector', 'course_link')
    prepopulated_fields = {'slug': ('name',)}
