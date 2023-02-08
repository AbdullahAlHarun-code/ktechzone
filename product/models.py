from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
# Create your models here.
class CategoryImage(models.Model):
    image = models.ImageField(upload_to='web/category/images/', blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='images')    
    alt = models.CharField(max_length=150, blank=True)
    width = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.alt

class PhoneModel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    series = models.ForeignKey("Series", on_delete=models.CASCADE, related_name='phoneModels')
    
    image = models.ImageField(upload_to='web/model/images/', blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=150)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:phoneModels", args=[self.series.category.slug, self.series.slug,self.slug])

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Series(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='catSeries')
    image = models.ImageField(upload_to='web/series/images/', blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=150)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse("product:series", args=[self.category.slug,self.slug])

    def save(self, *args, **kwargs):  # new
        
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    text = models.CharField(blank=True, null=True, max_length=150)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:categoryDetail", args=[self.slug])

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='web/category/images/', blank=True, null=True)
    products = models.ForeignKey("Products", on_delete=models.CASCADE, related_name='images')    
    alt = models.CharField(max_length=150, blank=True)
    width = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.alt



class Condition(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Capacity(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=200)
    phoneModel = models.ForeignKey("PhoneModel", on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=200, null=False, unique=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:products", args=[self.phoneModel.series.category.slug, self.phoneModel.series.slug,self.phoneModel.slug,self.slug])
    @property
    def get_capacity(self):
        cp=self.variation.all()
        cp_list = []
        for i in cp:
            cp_list.append(i.capacity.name)
        cp_list = sorted(set(cp_list), reverse=True)
        return cp_list
        #return (self.variation.all())
    @property
    def get_conditions(self):
        cp=self.variation.all()
        cp_list = []
        for i in cp:
            cp_list.append(i.conditions.name)
        cp_list = sorted(set(cp_list), reverse=True) 
        return cp_list
    
    @property
    def get_colors(self):
        cp=self.variation.all()
        cp_list = []
        for i in cp:
            cp_list.append(i.color.name)
        cp_list = sorted(set(cp_list), reverse=True) 
        return cp_list

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Reviews(models.Model):
    pass



class ProductVariation(models.Model):
    image = models.ImageField(upload_to='web/products/variations/images/', blank=True, null=True)
    
    capacity = models.ForeignKey(Capacity, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    conditions = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(default=0)
    was_price = models.FloatField(default=0)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Products, related_name='variation', on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.phoneModel} | {self.capacity} | {self.color} | {self.conditions} | {self.price} | Trade Price'

    class Meta:
        ordering = ['price']
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            new_slug = f'{self.product.phoneModel} {self.capacity} {self.color} {self.conditions}'
            self.slug = slugify(new_slug)
        return super().save(*args, **kwargs)

class Offer(models.Model):
    badge = models.CharField(max_length=100, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to='web/products/variations/offer/', blank=True, null=True)
    textColor = models.CharField(max_length=20, blank=True, null=True)
    bgColor = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)
    pVariation = models.ForeignKey(ProductVariation, related_name='offer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.badge

# class Supplier(models.Model):
#     name = 
#     phone = 
#     landline =
#     address = 
#     note = 
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     icon = models.ImageField(upload_to='web/supplier/', blank=True, null=True)
