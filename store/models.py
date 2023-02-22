from django.db import models
from store_custom.models import CategoryBlock
# Create your models here.
class StoreCollection(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=200)
    store_collection = models.ForeignKey(StoreCollection, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class SubCollection(models.Model):
    name = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class SubSubCollection(models.Model):
    name = models.CharField(max_length=200)
    sub_collection = models.ForeignKey(SubCollection, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
