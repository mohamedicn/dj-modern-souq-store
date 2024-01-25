from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "product/%s.%s"%(instance.slug,extension) 

class Product(models.Model):
    PRDname=models.CharField(max_length=100,verbose_name=_("product name"))
    PRDcategory=models.ForeignKey('Category',limit_choices_to={'CATParent__isnull' : False},on_delete=models.CASCADE,blank=True, null=True,verbose_name=("Categery"))
    PRDBrand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True, null=True,verbose_name=("Brand"))
    PRDDesc=models.TextField(verbose_name=_("Product Descripton"))
    PRDIImage=models.ImageField(upload_to=image_upload ,verbose_name=("Image"),blank=True, null=True)
    
    
    PRDPrice=models.DecimalField(max_digits=5,decimal_places=0 , verbose_name=_("Price"))
    PRDPriceDiscount=models.DecimalField(max_digits=5,decimal_places=0 , verbose_name=_("discount") ,default='0')
    PRDCost=models.DecimalField(max_digits=5,decimal_places=0,verbose_name=_("Cost"),blank=True,null=True)
    
    
    PRDCreated=models.DateTimeField(verbose_name=_("Created At"), default=datetime.now)
    slug = models.SlugField(blank=True ,null=True)
    PRDIs_Active=models.BooleanField(default=False ,verbose_name=_("Active"))
    PRDNew=models.BooleanField(default=True ,verbose_name=_("New-Product"))
    PRDSeller=models.BooleanField(default=False ,verbose_name=_("Bestseller"))
    
    @property
    def PRDCostValue(self):
        return self.PRDPrice - self.PRDPriceDiscount

    def save(self,*args,**kwargs):
        self.slug= slugify(self.PRDname)
        self.PRDCost = self.PRDCostValue
        super(Product,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.PRDname
    
    # def __str__(self) -> str:
    #     return self.PRDNew
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering= ['PRDPriceDiscount']
        ordering= ['-PRDNew']
            
            
class ProductImage(models.Model):
    PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE ,verbose_name=("product"))
    PRDIImage=models.ImageField(upload_to='product/' ,verbose_name=("Image"))
    def __str__(self) -> str:
        return str(self.PRDIProduct)

class Category(models.Model):
    CATName=models.CharField(max_length=50,verbose_name=("Name"))
    CATParent=models.ForeignKey('self',limit_choices_to={'CATParent__isnull' : True},on_delete=models.CASCADE,blank=True, null=True,verbose_name=("Main Category"))
    CATDes=models.TextField(verbose_name=("Description"))
    CATImg=models.ImageField(upload_to='category',verbose_name=("Images"))
    def __str__(self):
        return self.CATName
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
class Product_ALternative (models.Model):
    PALNProduct=models.ForeignKey(Product ,on_delete=models.CASCADE,related_name='main_product',verbose_name=("Product"))
    PALNAlternatives=models.ManyToManyField(Product,related_name='alternative_product',verbose_name=("Alternative"))
    class Meta:
        verbose_name = _("Product_ALternative")
        verbose_name_plural = _("Product_ALternatives")

    def __str__(self):
        return str(self.PALNProduct)

class Product_Accessories (models.Model):
    PACCProduct=models.ForeignKey(Product ,on_delete=models.CASCADE,related_name='mainAccessory_product',verbose_name=("Product"))
    PACCAlternatives=models.ManyToManyField(Product,related_name='Accessory_product',verbose_name=("Accessory"))

    class Meta:
        verbose_name = _("Product_Accessory")
        verbose_name_plural = _("Product_Accessories")

    def __str__(self):
        return str(self.PACCProduct)
