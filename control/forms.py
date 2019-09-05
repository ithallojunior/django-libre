from django import forms
from .models import Product, Order



class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'qtd']

        #Changing the name to be shown
        Product._meta.get_field('name').verbose_name = 'Nome'
        Product._meta.get_field('price').verbose_name = 'Valor unitário'
        Product._meta.get_field('qtd').verbose_name = 'Quantidade em estoque'



class OrderForm (forms.ModelForm):
    class Meta:
        model = Order
        fields = ['qtd', 'client', 'date', 'address', 'sender', 'status']


        #Changing the name to be shown
        Order._meta.get_field('qtd').verbose_name = 'Quantidade'
        Order._meta.get_field('client').verbose_name = 'Solicitante'
        Order._meta.get_field('date').verbose_name = 'Data do pedido'
        Order._meta.get_field('address').verbose_name = 'Endereço do solicitante'
        Order._meta.get_field('sender').verbose_name = 'Despachante'
        Order._meta.get_field('status').verbose_name = 'Situação do pedido'
