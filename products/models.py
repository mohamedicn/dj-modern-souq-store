from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "product/%s.%s"%(instance.slug,extension) 

class Product(models.Model):
    PRDname=models.CharField(max_length=300,verbose_name=_("product name"))
    PRDIImage=models.ImageField(upload_to=image_upload ,verbose_name=("Image"),blank=True, null=True)
    PRDDesc=models.TextField(verbose_name=_("Product Descripton"))
    
    PRDquantity=models.DecimalField(max_digits=10,decimal_places=0 , verbose_name=_("َQuantity") ,default='0')
    purchasingprice=models.DecimalField(max_digits=10,decimal_places=0,verbose_name=_("Purchasing Price") ,default='0')
    
    PRDcategory=models.ForeignKey('Category',limit_choices_to={'CATParent__isnull' : False},on_delete=models.CASCADE,blank=True, null=True,verbose_name=("Categery"))
    PRDBrand=models.ForeignKey('Brand',on_delete=models.CASCADE,blank=True, null=True,verbose_name=("Brand"))
    
    PRDPrice=models.DecimalField(max_digits=5,decimal_places=0 , verbose_name=_("Price"))
    PRDPriceDiscount=models.DecimalField(max_digits=5,decimal_places=0 , verbose_name=_("discount") ,default='0')
    PRDCost=models.DecimalField(max_digits=5,decimal_places=0,verbose_name=_("Cost"),blank=True,null=True)
    
    
    PRDCreated=models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
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
        
    def __str__(self):
        return self.PRDname
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering= ['PRDPriceDiscount']
        ordering= ['-PRDNew']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
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
        
        
        
class Brand(models.Model):
    BRDName=models.CharField(max_length=40,verbose_name=("Name"))
    BRDDesc=models.TextField(blank=True, null=True,verbose_name=("Description"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRDName