from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'order-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'order-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'order-input'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'order-input'}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'order-input'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'order-input'}))
    flat = forms.CharField(label='Квартира', widget=forms.TextInput(attrs={'class': 'order-input'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone',  'city', 'address', 'flat']


