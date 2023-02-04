from django.contrib import admin

from robotics.admin import TechnologiesImgAdmin, TechnologiesAdmin
# Register your models here.
from .models import *


class TechnologiesVisionImgAdmin(TechnologiesImgAdmin):
    pass


@admin.register(Technologies)
class TechnologiesVisionAdmin(TechnologiesAdmin):
    pass
