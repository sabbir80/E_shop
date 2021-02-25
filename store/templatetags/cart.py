from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if id==str(product.id):
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if id==str(product.id):
            return cart.get(id)
    return False
@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='total_price')
def total_price(product,cart):
    sum=0
    for i in product:
        sum+=price_total(i,cart)
    return sum

@register.filter(name='currency')
def currency(num):
    return "৳"+str(num)







