from django.contrib.auth import logout
from django.http import response
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Product, Category
from cart.cart import Cart

def product_list(request, category_slug=None):
    print(request.GET.get('referal', None))
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart': cart})


def product_detail(request, slug, product_id):
    product = get_object_or_404(Product, id=product_id, slug=slug, available=True)
    # if 'viewed_products' in request.session:
    #     request.session['viewed_products'].append(product.slug)
    #     request.session.modified = True
    # else:
    #     request.session['viewed_products'] = []
    #     request.session['viewed_products'].append(product.slug)
    #     request.session.modified = True
    return render(request, 'product_detail.html', {'product': product})


@require_POST
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.description = request.POST.get('product_description')
    product.amount = request.POST.get('product_amount')
    product.save()
    return render(request, 'product_detail.html', {'product': product})


def admin_logout(request):
    logout(request)
    return redirect('shop:main')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
