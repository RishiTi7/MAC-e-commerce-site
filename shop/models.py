from django.db import models

# Create your models here. here we are inheriting models
# here we used default value = null or 0 because when we created the db at first we didnt create all this additional files such as images etc so its like shouls i overwrite the db content, so we put the default value
class Product(models.Model):
    product_id = models.AutoField  # this increments the products in the db
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name  # to display the product name dynamically


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60, default="")
    phone = models.IntegerField(default="")
    message = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id =models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=500)    
    amount = models.IntegerField(default= 0)
    email = models.CharField(max_length=500)  
    phone = models.IntegerField()
    address = models.CharField(max_length=5009)  
    state = models.CharField(max_length=500)  
    city =models.CharField(max_length=100,default="")
    zip_code = models.CharField(max_length=500)      


class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc
        

