from django.contrib import admin
from.models import Product ,ProductImage,Category,Product_ALternative , Product_Accessories
class productAdmin(admin.ModelAdmin):
    list_display= ['PRDname','PRDCreated','PRDIs_Active','PRDNew','PRDSeller','PRDPrice','PRDPriceDiscount','PRDCost']
    list_editable= ['PRDIs_Active','PRDNew','PRDSeller']
    search_fields=['PRDname']
    # list_filter=['PRDname']
    # def combine_PRDPrice_and_PRDCost(self,ob):
    #  return "{} - {}".format(ob.PRDPrice,ob.PRDCost)

admin.site.register(Product,productAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_ALternative)
admin.site.register(Product_Accessories)
