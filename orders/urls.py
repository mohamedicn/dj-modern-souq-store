from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ajax_check_coupon
app_name='orders'


urlpatterns = [
    path('add_to_cart' , views.add_to_cart , name='add_to_cart'),
    path('cart' , views.cart , name='cart'),
    path('discount_value' , views.discount_value , name='discount_value'),
    path('ajax/check-coupon/', ajax_check_coupon, name='ajax_check_coupon'),
    path('remove_from_Cart/<int:orderdetials_id>' , views.remove_from_Cart , name='remove_from_Cart'),
    path('clear_Cart' , views.clear_Cart , name='clear_Cart'),
    path('add_qty/<int:orderdetials_id>' , views.add_qty , name='add_qty'),
    path('sub_qty/<int:orderdetials_id>' , views.sub_qty , name='sub_qty'),
    # path('payment' , views.ckeck_out , name='ckeck_out'),
    path('payment' , views.paypal_pament , name='paypal_pament'),
    path('order_completed' , views.order_completed , name='order_completed'),
]