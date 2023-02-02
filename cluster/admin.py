from django.contrib import admin

from .models import News, NewsImg, NewsVideo


# Register your models here.

class NewsImgAdmin(admin.TabularInline):
    model = NewsImg
    fields = ('image',)
    extra = 0


class NewsVideoAdmin(admin.TabularInline):
    model = NewsVideo
    fields = ('video_link',)
    extra = 0

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = (NewsImgAdmin, NewsVideoAdmin)
    search_fields = ('title',)
    fields = ('title', 'slug', 'content', 'time_created', 'time_updated')
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ('time_created', 'time_updated',)