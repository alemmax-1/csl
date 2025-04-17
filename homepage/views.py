from django.shortcuts import render
from .models import Carousel, Marketing
# Create your views here.
def index(request):
    # Recupera gli oggetti del modello Carousel
    carousel_items = Carousel.objects.all()
    # Recupera gli oggetti del modello Marketing
    marketing_items = Marketing.objects.all()
    # Passa gli oggetti al template
    context = {
        'carousels': carousel_items,
        'marketings': marketing_items,
    }
    
    return render(request, 'homepage/index.html', context)