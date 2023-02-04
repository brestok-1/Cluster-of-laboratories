from django.contrib import admin

from robotics.models import TechnologiesRobotics, TechnologiesImgRobotics


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgRobotics
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesRobotics)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
