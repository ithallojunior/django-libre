from django.shortcuts import render, redirect
from .models import Product, Order, STATUS_CHOICES
from .forms import ProductForm, OrderForm
from django import forms

# Create your views here.

#CREATE
def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form':form})

# READ
def list_products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products':products})

#UDPATE
def update_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form':form, 'product':product})

#DELETE
def delete_products(request, id):
    product = Product.objects.get(id=id)
    reasons = "Há pedidos que precisam que produto %s exista."%(product.name)

    if (list(Order.objects.filter(product_id=id)) != []):
        return render(request, 'cant.html', {'reasons': reasons})

    else:
        if request.method == 'POST': #when someone clicks the button it is a GET, so they need to confirm deletion
            product.delete()
            return redirect("list_products")


        return render(request, 'delete-confirm.html', {'product': product, 'mytype':'produto'})

##########################################################################################################
# Orders
#create_orders, this is the only order_something that receives a key from products
def create_orders(request, id):


    form = OrderForm(request.POST or None)

    if form.is_valid():
        #print("\n\n", form.cleaned_data, "\n\n")
        data = form.cleaned_data

        #checking if there is enough of something
        if (data['qtd'] > Product.objects.get(id=id).qtd):
            reasons = "A quatidade solicitada excede a disponível."
            return render(request, 'cant.html', {'reasons': reasons})

        else:
            myorder = Order(product_id=id, qtd=data['qtd'], client=data['client'], date=data['date'], address=data['address'], sender=data['sender'], status=data['status'] )
            myorder.save()

            #removing the ordered products from the available ones
            b_product = Product.objects.get(id=id)
            b_product.qtd -= data["qtd"]
            b_product.save()

            return redirect('list_orders')

    return render(request, 'orders-form.html', {'form':form})


# READ orders
def list_orders(request):
    orders = Order.objects.all()
    if (list(orders)!=[]):
        to_show = True
    else:
        to_show = False

    #select product_id from...
    pre_products = list(map(lambda x: list(Product.objects.filter(id=x['product_id']).values('name', 'price'))[0], list(orders.values('product_id'))))

    products_and_order = zip(orders, pre_products)

    return render(request, 'orders.html', {'products':products_and_order, 'to_show':to_show})

#UDPATE
# when updating and order, it checks if the number of products would change
def update_orders(request, id):
    order = Order.objects.get(id=id)
    previous_qtd = order.qtd

    form = OrderForm(request.POST or None, instance=order)


    if form.is_valid():
        data = form.cleaned_data
        diff = data['qtd'] - previous_qtd
        #checking if qtd has changed

        if (diff > Product.objects.get(id=order.product_id).qtd):
            reasons = "A quatidade solicitada excede a disponível."
            return render(request, 'cant.html', {'reasons': reasons})

        #changing  the ordered products as requested
        b_product = Product.objects.get(id=order.product_id)
        b_product.qtd -= diff # if negative, it means some were remove from the order, which makes it increase
        b_product.save()

        form.save()
        return redirect('list_orders')

    return render(request, 'orders-form.html', {'form':form, 'order':order})

#DELETE
# if the product was not sent, it increases the amount available
def delete_orders(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST': #when someone clicks the button it is a GET, so they need to confirm deletion

        #if not sent, becomes available again
        if (order.status==STATUS_CHOICES[0][0]):
            b_product = Product.objects.get(id=order.product_id)
            b_product.qtd += order.qtd
            b_product.save()

        order.delete()
        return redirect("list_orders")


    return render(request, 'delete-confirm.html', {'order': "", 'mytype':'pedido'})
