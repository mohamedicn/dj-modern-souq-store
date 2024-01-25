from unicodedata import name
from django.urls import path ,include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='products'


urlpatterns = [
    path('',ProdcutListView.as_view(),name='product_list'),
    # path('',views.product_list,name='product_list'),
    path('more/<str:category_name>',ProdcutListView_More.as_view(),name='product_list_more'),
    path('<str:slug>',ProdcutDetailView.as_view(),name='product_detail'),
    
    # api
    # path('property/list',PropertyAPiList.as_view(),name='PropertyAPiList'),
    # path('property/list/<int:pk>',PropertyAPiDetail.as_view(),name='PropertyAPiDetail'),
]
