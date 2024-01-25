from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='product'


urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<str:slug>',views.product_detail,name='product_detail')
]
