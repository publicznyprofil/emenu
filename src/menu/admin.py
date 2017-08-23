from django import forms
from django.contrib import admin

from .models import (
    Menu,
    Dish,
)


class MenuFormAdmin(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = ('created', 'modified')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    form = MenuFormAdmin


class DishFormAdmin(forms.ModelForm):
    class Meta:
        model = Dish
        exclude = ('created', 'modified')


class DishAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'price', 'preparation_time', 'is_vegetarian', 'created')
    list_display_links = ('name',)
    form = DishFormAdmin


admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)
