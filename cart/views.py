from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from shop.views import Product

def show_cart(request):
    context = {
        'cart': Cart(request),
        'asd': 'dsa'
    }
    return render(request, 'cart_detail.html', context=context)

@require_POST
def cart_add(request, product_id, amount=1):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, amount=amount)
    return redirect('shop:main')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('shop:main')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
