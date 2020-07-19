from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    orignal_price = models.IntegerField(default=0)
    desc = models.CharField(max_length=350,default="")
    pub_date = models.DateField()
    image1 = models.ImageField(upload_to="WebKart/images",default="1")
    image2 = models.ImageField(upload_to="WebKart/images",default="2")
    image3 = models.ImageField(upload_to="WebKart/images",default="3")
    full_specs = models.CharField(max_length=1000,default="NA")
    warranty = models.CharField(max_length=350,default="NA")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50,default="none")
    email = models.CharField(max_length=50,default="none")
    city = models.CharField(max_length=50,default="none")
    state = models.CharField(max_length=20,default="none")
    mobile = models.CharField(max_length=20,default="none")
    suggestion = models.CharField(max_length=1000,default="none")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    address= models.CharField(max_length=200,default='')
    city = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    zip_code = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=50,default='00000')

class OrdersUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000,default='Checking Order Details')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

