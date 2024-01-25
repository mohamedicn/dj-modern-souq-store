from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='accounts'


urlpatterns = [
    path('signup',views.signup ,name='signup'),
    path('check_email_availability/', views.check_email_availability, name='check_email_availability'),
    path('signin',views.signin ,name='signin'),
    path('activate_account/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('log_out',views.log_out ,name='log_out'),
    path('profile/<slug:slug>',views.profile ,name='profile'),
    path('profile/<slug:slug>/order',views.order ,name='order'),
    path('profile/<slug:slug>/order/<int:pk>/detail',views.order_details ,name='order_details'),
    path('productfavorites/<str:slug>',views.product_favorites ,name='product_favorites'),
    path('profile/<slug:slug>/product-favorites',views.showproduct_favorites ,name='showproduct_favorites'),
    path('profile/<slug:slug>/editprofile',views.edit_profile ,name='edit'),
]
