from django.contrib import admin

from . import models

@admin.register(models.Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
