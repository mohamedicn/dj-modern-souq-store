from django.contrib import admin
from.models import *
# Register your models here.
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin

class ProductImportExportModelAdmin(ImportExportModelAdmin):
    pass

class productAdmin(admin.ModelAdmin):
    list_display= ['PRDname','PRDCreated','PRDcategory','PRDIs_Active','PRDNew','PRDSeller','PRDPrice','PRDPriceDiscount','PRDCost']
    list_editable= ['PRDIs_Active','PRDNew','PRDSeller']
    search_fields=['PRDname']
    fieldsets = (
        (_("Info"), {
            'fields': ('PRDname', 'PRDcategory',
                        'PRDBrand','PRDDesc','PRDquantity',
                        'purchasingprice','PRDIImage')
        }),
        (_("for Saleing"), {
            'fields': ('PRDPrice','PRDPriceDiscount',
                        'PRDCost','PRDIs_Active',
                        'PRDNew','PRDSeller')
        }),
    )
    
class productAdminn(ProductImportExportModelAdmin,productAdmin):
    pass

admin.site.register(Product,productAdminn)
admin.site.register(Category)
admin.site.register(Brand)
