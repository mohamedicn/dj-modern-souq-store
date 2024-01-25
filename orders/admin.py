from django.contrib import admin

# Register your models here.
from.models import Order,OrderDetails,Checkout,Discount_Coupon


class Property_Detail(admin.TabularInline):
    model = OrderDetails 
    extra = 1
    readonly_fields = ('cost','total',) 
    
class OrderAdmin(admin.ModelAdmin):
    inlines=[Property_Detail]
    readonly_fields = ('user','is_finished','all_total','coupon',)

class OrderDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('product','order','total','cost',)

class CheckoutAdmin(admin.ModelAdmin):
    readonly_fields = ('order',)
    
class Discount_CouponAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display= ['user','name_coupon','discount_value',]
    search_fields=['user__username',]
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)
    
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetails,OrderDetailsAdmin)
admin.site.register(Checkout,CheckoutAdmin)
admin.site.register(Discount_Coupon,Discount_CouponAdmin)