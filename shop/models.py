from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images/", default="")
    publish_date = models.DateField()

    # Return name of the product
    def __str__(self):
        return self.product_name
