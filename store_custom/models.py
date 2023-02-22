from django.db import models

# Create your models here.
class CategoryBlock(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

# class StoreCategory(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)
#     def __str__(self):
#         return self.name