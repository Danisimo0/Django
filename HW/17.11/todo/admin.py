from django.contrib import admin
from todo import models as django_models

# Register your models here.

# admin.site.site_header = '1111111111'  # default: "Django Administration"
# admin.site.index_title = '22222222222'  # default: "Site administration"
# admin.site.site_title = '333333333'  # default: "Django site admin"


class Users(admin.ModelAdmin):
    """
    Settings admin page for Todo
    """
    list_display = (
        'id',
        'user_nickname',
        'user_password'
    )
    list_display_links = (
        'id',
        'user_nickname',
        'user_password'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'user_nickname',
        'user_password'
    )
    search_fields = (
        'id',
        'user_nickname',
        'user_password'
    )
    fieldsets = (
        ("ID", {"fields": ('id',)}),
        ("Nickname", {"fields": ('user_nickname',)}),
        ("Password", {"fields": ('user_password',)}),
    )

class Tasks(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (
        'id',
        'author_id',
        'title',
        'description',
    )
    list_display_links = (
        'id',
        'author_id',
        'title',
        'description',
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'author_id',
        'title',
        'description',
    )
    search_fields = (
        'id',
        'author_id',
        'title',
        'description',
    )
    fieldsets = (
        ("ID", {"fields": ('id',)}),
        ("ID author", {"fields": ('author_id',)}),
        ("Text", {"fields": ('title',)}),
        ("About", {"fields": ('description',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
admin.site.register(django_models.Tasks, Tasks)  # complex register model