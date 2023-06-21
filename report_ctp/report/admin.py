from django.contrib import admin

from .models import AuthorRep, Type, Report

admin.site.empty_value_display = 'Не задано'

@admin.register(AuthorRep)
class AuthorRep(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Type)
class Type(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Report)
class Type(admin.ModelAdmin):
    list_display = (
        'number_report',
        'date_add_report',
    )