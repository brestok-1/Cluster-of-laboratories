from django.contrib import admin

from .models import News, NewsImg, Students


# Register your models here.

class NewsImgAdmin(admin.TabularInline):
    model = NewsImg
    fields = ('image',)
    extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = (NewsImgAdmin,)
    search_fields = ('title',)
    fields = ('title', 'slug', 'content', 'time_created', 'time_updated', 'video_link')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('time_created', 'time_updated',)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}
