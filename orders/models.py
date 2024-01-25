from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from decimal import Decimal
from audioop import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime

from creditcards.models import CardNumberField,CardExpiryField,SecurityCodeField

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=(('تم الشحن', 'تم الشحن'), ('جاري الشحن', 'جاري الشحن')),default='جاري الشحن',)
    coupon=models.ForeignKey('Discount_Coupon', verbose_name=_("Discount Coupon"), on_delete=models.SET_NULL,default=None, null=True, blank=True)
    order_date= models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    is_finished = models.BooleanField()
    all_total=models.IntegerField(default=0,verbose_name=_("Total"))
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return 'User: ' +  self.user.username + ', Order id: ' + str(self.id) + ', status : ' + self.status

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
    def get_discount_value(self):
        if self.coupon:
            return self.coupon.discount_value
        return 0
    def update_total(self):
        total = sum(order_detail.total for order_detail in self.orderdetails_set.all())
        self.all_total = total
        self.all_total = self.all_total - self.get_discount_value()
        self.save()

class OrderDetails(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderdetails_set')
    cost=models.DecimalField(max_digits=5,decimal_places=0,verbose_name=_("Cost"))
    quantity=models.IntegerField()
    total=models.IntegerField(default=0)
    
    @property
    def TotalValue(self):
        if self.cost is not None and self.quantity is not None:
            return self.cost * Decimal(self.quantity)
        return 0
    def save(self, *args, **kwargs):
        try:
            product = self.product
            self.cost = product.PRDCost
            
        except Product.DoesNotExist:
            pass
        self.total = self.TotalValue
        super(OrderDetails, self).save(*args, **kwargs)
        self.order.update_total()
    def delete(self, *args, **kwargs):
        super(OrderDetails, self).delete(*args, **kwargs)
        
        # Call the update_total method of the related Order
        self.order.update_total()

    class Meta:
        verbose_name = _("OrderDetails")
        verbose_name_plural = _("OrderDetailss")
    def __str__(self):
        return 'User: ' +  self.order.user.username + 'Product: '+ self.product.PRDname + 'Order id: ' + str(self.order.id)
    def get_absolute_url(self):
        return reverse("OrderDetails_detail", kwargs={"pk": self.pk})

class Discount_Coupon(models.Model):
    user=models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name_coupon=models.CharField(max_length=10,verbose_name=_("coupon"))
    discount_value=models.IntegerField()
    class Meta:
        verbose_name = _("Discount Coupon")
        verbose_name_plural = _("Discount Coupons")
    def __str__(self):
        return 'User : ' +  self.user.username + ' , discount value : ' + str(self.discount_value) + ' , name coupon : ' + str(self.name_coupon) + ' , coupon id : ' + str(self.id)

class Checkout(models.Model):
    """Model definition for Checkout."""
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)
    phone=models.CharField(max_length=20,verbose_name=_("phone"))
    cardholder=models.CharField(max_length=20,verbose_name=_("Card Holder"))
    cardnumber=CardNumberField(verbose_name=_("Card Number"),max_length=16)
    expire=CardExpiryField(verbose_name=_("Exepire Date"))
    security=SecurityCodeField(verbose_name=_("CCV"))
    order_delivery_date= models.DateTimeField(verbose_name=_("Delivery Date"),blank=True, null=True)

    def __str__(self):
        return 'User: ' +  self.order.user.username + ' --> Order id: ' + str(self.id)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        

