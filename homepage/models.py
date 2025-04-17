from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

class AbstractContent(models.Model):
    """
    Abstract model for shared carousel fields.
    """
    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        
class Carousel(AbstractContent):
    """
    Modello per la gestione delle immagini del carosello.
    """
    # image = models.ImageField(upload_to='carousel_images/')
    order = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f"{self.title} - {self.order}"


class Marketing(AbstractContent):
    """
    Modello per la gestione delle immagini del marketing.
    """
    order = models.IntegerField(default=0, unique=True, validators=[MinValueValidator(0), MaxValueValidator(2)])
    def __str__(self):
        return f"{self.title} - {self.order}"