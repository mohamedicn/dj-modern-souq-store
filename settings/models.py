from django.db import models
from django.utils.text import slugify
# Create your models here.

def settings_img(instance,filename):
    imagename , extension = filename.split(".")
    return "postimg/%s.%s"%(instance.site_name,extension)

class Settings(models.Model):
    """Model definition for Settings."""
    site_name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to=settings_img)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    description=models.TextField(max_length=500)
    fb_link=models.URLField(max_length=200)
    inst_link=models.URLField(max_length=200)
    twitter_link=models.URLField(max_length=200)
    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.site_name
    
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "img_ads/%s.%s"%(instance.slug,extension) 

class Nav_ads(models.Model):

    # TODO: Define fields here
    number=models.IntegerField(default=0)
    slug = models.SlugField(blank=True ,null=True)
    nav_ads_image=models.ImageField(upload_to=image_upload ,verbose_name=("Image"))
    
    class Meta:

        verbose_name = 'Nav_ads'
        verbose_name_plural = 'Nav_ads'

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        if not self.number:
            max_number = Nav_ads.objects.all().aggregate(models.Max('number'))['number__max']
            self.number = max_number + 1 if max_number is not None else 1
        self.slug= slugify(self.number)
        super(Nav_ads, self).save(*args, **kwargs)
