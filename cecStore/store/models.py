from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from user.models import User

class Product(models.Model):
    pname = models.CharField(max_length=30)
    product_id = models.AutoField(primary_key=True)
    p_short = models.CharField(max_length=10)
    mrp = models.FloatField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20,blank=True)
    spec = models.CharField(max_length=200,blank=True)
    desc = models.CharField(max_length=300,blank=True)
    seller = models.EmailField(max_length=70,blank=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)




    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.product_id})

    def __str__(self):
        return self.pname
class Purchase(models.Model):
    purch_id = models.AutoField(primary_key=True)
    adm_no = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date=models.DateField()
    remarks = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    responded = models.IntegerField(default=0)
    placed= models.IntegerField(default=0)

    total = models.FloatField(default=0 , null=True)
    def __str__(self):
        return str(self.purch_id)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.purch_id})

class Plist(models.Model):
    purch_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    tfield = models.AutoField(primary_key=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.tfield)
