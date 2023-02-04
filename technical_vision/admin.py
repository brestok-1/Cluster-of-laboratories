from django.contrib import admin

from technical_vision.models import TechnologiesVision, TechnologiesImgVision


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImgVision
    fields = ('img',)
    extra = 1


@admin.register(TechnologiesVision)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
