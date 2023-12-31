from django.shortcuts import render, redirect
from products.models import Product
from reviews.models import Review
from history.models import ProductViewHistory
from products.models import Product
from reviews.models import Review
from history.models import ProductViewHistory
from django.conf.urls import handler404
from . import views

def index(request):
    """ A view to return the index page """

    latest_reviews = Review.objects.order_by('-created_at')[:3]
    products = Product.objects.all()[:6] 

    # Initialize an empty query set for home_view_history
    home_view_history = None

    # Check if user is authenticated
    if request.user.is_authenticated:
        # Fetch the user's view history if they are authenticated
        home_view_history = ProductViewHistory.objects.filter(user=request.user)[:6]

    # Pass the history to the template, will be None if user is not authenticated
    return render(request, 'home/index.html', {
        'latest_reviews': latest_reviews, 
        'products': products, 
        'home_view_history': home_view_history
    })


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        return redirect('contact')

    return render(request, 'home/contact.html')

def special_offers(request):
    """ A view to return the special offers page """
    return render(request, 'home/special_offers.html')

def my_custom_page_not_found_view(request, exception):
    """
    Custom 404 error handler.
    Renders a custom 404 error page when a requested resource is not found.
    """
    return render(request, '404.html', {}, status=404)