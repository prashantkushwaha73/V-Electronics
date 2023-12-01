from django.db import models

# Create your models here.

class Prod(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=300)
    desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.desc







    