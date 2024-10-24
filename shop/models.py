import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank=True,default=name)
    details = models.TextField(blank=True,default=name)
    image = models.ImageField(upload_to='productImages/')
    tag = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class RelatedImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='relatedImages/')