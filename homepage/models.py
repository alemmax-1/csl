from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

class Carousel(models.Model):
    """
    Modello per la gestione delle immagini del carosello.
    """
    # image = models.ImageField(upload_to='carousel_images/')
    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(
        default=0, unique=True,
        validators=[MinValueValidator(0), MaxValueValidator(4)]
        )

    def __str__(self):
        return f"{self.title} - {self.order}"