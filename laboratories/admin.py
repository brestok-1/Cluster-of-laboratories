from django.contrib import admin

from laboratories.models import Laboratory, AboutLaboratory, AboutLaboratoryImg


# Register your models here.
@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class AboutLaboratoryImgAdmin(admin.TabularInline):
    model = AboutLaboratoryImg
    fields = ('owner', 'img')
    extra = 0


@admin.register(AboutLaboratory)
class AboutLaboratoryAdmin(admin.ModelAdmin):
    fields = ('owner', 'slug', 'content')
    # prepopulated_fields = {'slug': ('owner.name')}
    inlines = (AboutLaboratoryImgAdmin,)
