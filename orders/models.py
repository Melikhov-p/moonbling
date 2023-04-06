from django.core.validators import MaxValueValidator
from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    delivery = models.BooleanField(verbose_name='Доставка', default=False)
    address = models.CharField(max_length=250, verbose_name='Адрес', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='Город', default='Белгород')
    flat = models.CharField(max_length=10, verbose_name='Квартира', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', null=True, blank=True, max_length=11)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', verbose_name='Товар', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    amount = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.amount
