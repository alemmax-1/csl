from django.shortcuts import render
from .models import Carousel
# Create your views here.
def index(request):
    # Recupera gli oggetti del modello Carousel
    carousel_items = Carousel.objects.all()
    
    # Passa gli oggetti al template
    context = {
        'carousels': carousel_items,
    }
    
    return render(request, 'homepage/index.html', context)