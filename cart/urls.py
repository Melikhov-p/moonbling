from . import views
from django.conf.urls.static import static
from django.urls import path, include
from moonbling import settings


urlpatterns = [
    path('', views.show_cart, name='cart_detail'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<str:product_id>', views.cart_remove, name='cart_remove'),
    path('clear/', views.cart_clear, name='cart_clear')
]

