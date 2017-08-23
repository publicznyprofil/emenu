from django.db import models


class Menu(models.Model):
    name = models.CharField('nazwa', max_length=256, unique=True)
    description = models.CharField('opis', max_length=1024)
    created = models.DateTimeField('stworzono', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class Dish(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField('nazwa', max_length=256)
    description = models.CharField('opis', max_length=1024)
    price = models.DecimalField('cena', max_digits=5, decimal_places=2)
    preparation_time = models.DurationField('czas przygotowania')
    is_vegetarian = models.BooleanField('danie wegetariańskie', default=False)
    created = models.DateTimeField('stworzono', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Danie'
        verbose_name_plural = 'Dania'

    def __str__(self):
        return self.name
