from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=200, verbose_name='Слаг', db_index=True)
    image = models.ImageField(upload_to='products/images', verbose_name='Изображение', blank=True, default='default/default_product_image.png')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, verbose_name='Цена', decimal_places=2)
    amount = models.PositiveIntegerField(verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
