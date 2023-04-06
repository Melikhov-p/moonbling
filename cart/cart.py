from decimal import Decimal
from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        # Обновление сессии cart
        self.session['cart'] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def add(self, product, amount=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[str(product_id)] = {'amount': amount, 'price': str(product.price)}
        else:
            self.cart[str(product_id)]['amount'] += amount
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в корзине и получение их из БД"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = Decimal(item['price']) * item['amount']
            yield item

    def __len__(self):
        return sum(item['amount'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['amount'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.session.modified = True
