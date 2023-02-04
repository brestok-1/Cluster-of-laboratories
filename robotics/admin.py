from django.contrib import admin

from robotics.models import Technologies, TechnologiesImg


class TechnologiesImgAdmin(admin.TabularInline):
    model = TechnologiesImg
    fields = ('img',)
    extra = 1


# Register your models here.
@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    inlines = (TechnologiesImgAdmin,)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

