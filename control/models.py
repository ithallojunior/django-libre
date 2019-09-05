from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    qtd = models.PositiveIntegerField()



    def __str__(self):
        return self.name

STATUS_CHOICES = [
    ('Pendente de envio', 'Pendente de envio'),
    ('Enviado', 'Enviado'),
    ('Entregue', 'Entregue')
]


class Order(models.Model):
    product_id = models.IntegerField() # to be related with the product
    qtd = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    client = models.CharField(max_length=200)
    date = models.DateField()
    address = models.CharField(max_length=400)
    sender = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
