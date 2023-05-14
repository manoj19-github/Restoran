from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100,default="")
    img = models.ImageField(upload_to='pics',default="/")
    desc = models.TextField(default="")
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default = False)
    
     