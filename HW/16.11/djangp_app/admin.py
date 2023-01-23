from django.contrib import admin
from django_app import models
from .models import profile


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'description',
    )
    list_filter = (
        'title',
        'description',
    )
    search_fields = (
        'title',
        'description',
    )
    fieldsets = (
        ("Main", {"fields": ('title',)}),
        ("Additional", {"fields": ('description',)}),
    )


class TodosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'description',
    )
    list_filter = (
        'title',
        'description',
    )
    search_fields = (
        'title',
        'description',
    )
    fieldsets = (
        ("Main", {"fields": ('title',)}),
        ("Additional", {"fields": ('description',)}),
    )


admin.site.register(models.Todo, TodosAdmin)


admin.site.register(profile)