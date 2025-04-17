from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """
    Modello per la gestione delle immagini del carosello.
    """
    list_display = ('title', 'description', 'order')
    list_filter = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)