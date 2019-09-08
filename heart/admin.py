from django.contrib import admin

from . import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'subgroups', 'delegate')
    list_filter = ['year', 'subgroups']


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'members')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'year', 'quarter')
    list_filter = ['year', 'quarter']
