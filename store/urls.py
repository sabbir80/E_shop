from django.urls import path
from.import views
from.views import login,index,signup,Cart,Order
from .views import Checkout
urlpatterns=[
    path('',index.as_view(), name='index'),
    path('signup/', signup.as_view(), name='signup'),
    path('login/', login.as_view(),name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', Cart.as_view(),name='cart'),
    path('order/', Order.as_view(),name='order'),
    path('checkout', Checkout.as_view(), name='checkout'),
]