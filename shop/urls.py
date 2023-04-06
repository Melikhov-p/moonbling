from . import views
from django.conf.urls.static import static
from django.urls import path, include
from moonbling import settings

urlpatterns = [
    path('', views.product_list, name='main'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('shop/<str:slug>/<int:product_id>', views.product_detail, name='product_detail'),
    path('shop/about', views.about, name='about'),
    path('shop/contacts', views.contacts, name='contacts'),
    path('product_update/<int:product_id>', views.product_update, name='product_update'),
    path('admin_logout/', views.admin_logout, name='admin_logout')
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
