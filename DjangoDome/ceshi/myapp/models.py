from django.db import models
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    status = models.SmallIntegerField
    create_time = models.DateTimeField
