from django.contrib import admin

# Register your models here.
class NodeManager(admin.ModelAdmin):
    list_display = ['id','title','user']
from . import models
admin.site.register(models.Note,NodeManager)