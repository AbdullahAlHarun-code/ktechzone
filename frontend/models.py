from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 

class PageCategory(models.Model):
    name = models.CharField(max_length=150)
    text = models.CharField(blank=True, null=True, max_length=150)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):pass
        #return reverse("product:categoryDetail", args=[self.slug])

class Carsoul(models.Model):
    image = models.ImageField(upload_to='web/page/slider/', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subTitle = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    query_text= models.CharField(max_length=250,blank=True, null=True)
    pageSection = models.ForeignKey("PageSection", on_delete=models.CASCADE, related_name='carousel')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title
    
class SectionText(models.Model):
    text = models.CharField(max_length=250)
    query_text= models.CharField(max_length=250)
    description= models.TextField(blank=True, null=True)
    pageSection = models.ForeignKey("PageSection", on_delete=models.CASCADE, related_name='sectionText')

    def __str__(self):
        return self.text

class SectionImage(models.Model):
    image = models.ImageField(upload_to='web/page/category/images/', blank=True, null=True)
    pageSection = models.ForeignKey("PageSection", on_delete=models.CASCADE, related_name='sectionImage')    
    alt = models.CharField(max_length=150, blank=True)
    width = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    query_text = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.alt



class PageSection(models.Model):  
    name = models.CharField(max_length=150)
    pageCategory = models.ForeignKey("PageCategory", on_delete=models.CASCADE, related_name='allPageSection')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.pageCategory}'