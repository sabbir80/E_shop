from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Product,Category
from .models.Customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
# Create your views here.

class index(View):
    def get(self,request):
        product = Product.objects.all()
        category = Category.objects.all()
        context = {
            'products': product,
            'categories': category

        }
        return render(request, 'index.html', context)
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        print(product)
        cart=request.session.get('cart')
        print(cart)
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']= cart





        #print(request.session['cart'])



        return redirect('index')


class signup(View):
    def validateCustomar(self, customer):
        error_massage = None
        if not customer.first_name:
            error_massage = "first_name requried!!"
        elif not customer.last_name:
            error_massage = "last name requried!!"
        elif not customer.email:
            error_massage = "email is requried!!"
        elif customer.isExist():
            error_massage = "mail is already exist"

        return error_massage

    def register(self, request):
        postdata = request.POST
        firstname = postdata.get('first_name')
        lastname = postdata.get('last_name')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = make_password(postdata.get('password'))

        value = {
            'fn': firstname,
            'ln': lastname,
            'phn': phone,
            'email': email
        }
        customer = Customer(first_name=firstname,
                            last_name=lastname,
                            phone=phone,
                            email=email,
                            password=password
                            )
        error_massage = self.validateCustomar(customer)

        if not error_massage:

            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_massage,
                'value': value
            }
            return render(request, 'signup.html', data)
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        return self.register(request)


class login(View):

    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        postdata = request.POST
        email = postdata.get('email')
        password = postdata.get('password')
        check_mail = Customer.get_object_by_mail(email)
        error_massage = None


        if check_mail:

            flag = check_password(password,check_mail.password)
            if flag:
                request.session['customer_id'] = check_mail.id
                return redirect('index')
            else:
                error_massage = 'invalid email or password!!'
        else:
            error_massage = 'invalid email or password!!'


        return render(request, 'login.html',{'error':error_massage})


class Order(View):
    def get(self,request):
        return render(request, 'order/order.html')
    def post(self):
        pass

def logout(request):
    try:
        request.session.clear()
        #del request.session['customer_id']
        return redirect('index')
    except:
        return HttpResponse('no user logged in')

class Cart(View):
    def get(self,request):
        try:

            ids = list(request.session.get('cart').keys())
            product = Product.get_product_by_id(ids)
            # c = request.session.get('cart').values()
            context = {
                'product': product,
                # 'c':c
            }
            return render(request, 'order/cart.html', context)
        except:
            return render(request,'order/cart.html')
class Checkout(View):
    def post(self,request):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        customer=request.session.get('customer_id')
        print(phone,address,customer)
        return redirect('cart')






