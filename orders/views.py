from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST' and cart.__len__() != 0:
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         amount=item['amount'])
            cart.clear()
            return render(request, 'order_created.html', {'order': order})
        else:
            print(form.errors)
    else:
        form = OrderCreateForm
        return render(request, 'order_create.html', {'cart': cart, 'form': form})
