from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

class Tag(models.Model):
    label = models.CharField(max_length=255)
    def __str__(self):
        return self.label

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.tag.label
    
class Series(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name
class CatModel(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name
       
class Details(models.Model):
    label = models.CharField(max_length=255)
    series = GenericRelation(Series)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.label
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
class Collection(models.Model):
    name = models.CharField(max_length=255)
    collections = GenericRelation(CatModel)
    def __str__(self):
        return self.name



# class SubCategory(models.Model):
    
#     collections = models.CharField(max_length=100, choices=cc)
#     #collections = models.OneToOneField(Collection.objects.all().first().collections.all(), on_delete=models.CASCADE)
#     sub_categorys = GenericRelation(CatModel)
#     def __str__(self):
#         return self.collections.name
    
class PageCategory(models.Model):
    name = models.CharField(max_length=150)
    text = models.CharField(blank=True, null=True, max_length=150)
    tags = GenericRelation(Details)
    

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
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, default=PageCategory)
    # object_id = models.PositiveIntegerField(null=True, default=1)
    # content_object = GenericForeignKey('content_type', 'object_id')
    #texts = GenericRelation(SectionText, related_query_name='all_texts')
    #carsouls = GenericRelation(Carsoul)
    #images = GenericRelation(SectionImage, related_query_name='all_images')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.pageCategory}'