from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.models import ContentType
from .models import(
    PageCategory,
    Carsoul,
    SectionText,
    SectionImage,
    PageSection,
    Tag,
    TaggedItem,
    Details,
    Series,
    CatModel,
    Collection
)
class CatModelInline(GenericTabularInline):
    model = CatModel
    extra = 0
class SeriesInline(GenericTabularInline):
    model = Series
    extra = 0
class DetailsInline(GenericTabularInline):
    model = Details
    extra = 0

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name','get_collections',)
    inlines = [
        CatModelInline,
    ]
    @admin.display
    def get_collections(self, collection):
        cc = Collection.objects.all().first().collections.all()
        cc_tuple = []
        for x in cc:
            y = (x.id,x.name)
            cc_tuple.append(y)
        print(cc_tuple)
        test = ' | '.join([x.name for x in collection.collections.all()])
        #print(test)
        #print(Details(content_object=self))
        return test
admin.site.register(Collection, CollectionAdmin)
admin.site.register(CatModel)
class SeriesAdmin(admin.ModelAdmin):
    inlines = [
        SeriesInline,
    ]
class TagItemInline(admin.TabularInline):
    model = TaggedItem
    extra = 0
class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagItemInline,
    ]
admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem)
admin.site.register(Details, SeriesAdmin)
class CarsoulInline(admin.TabularInline):
    model = Carsoul
    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':30})},
    }
    extra = 0

class SectionTextInline(admin.TabularInline):
    model = SectionText
    extra = 0

class SectionImageInline(admin.TabularInline):
    model = SectionImage
    extra = 0

class PageSectionInline(admin.TabularInline):
    model = PageSection
    extra = 0


class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'get_tags')
    inlines = [
        DetailsInline,
        PageSectionInline,
        
    ]
    @admin.display
    def get_tags(self, pageCategory):
        test = ' | '.join([x.label for x in pageCategory.tags.all()])
        #print(test)
        #print(Details(content_object=self))
        return test
class PageSectionAdmin(admin.ModelAdmin):
    list_filter = ('pageCategory__name',)
    list_display = ('name', 'pageCategory')
    inlines = [
        DetailsInline,
        CarsoulInline,
        SectionTextInline,
        SectionImageInline,
    ]
    @admin.display
    def get_tags(self, page_section):
        all = page_section.details.all()
        t_sereis = ''
        for i in all:
            if i.series.all():
                y = i.label+'('+' | '.join([x.name for x in i.series.all()])+')'
                
            else:
                y = ' | '+i.label 
            t_sereis += y

        series_all = page_section.details.all()
        print(all)
        #print(GenericRelation(Details, related_query_name='pagesection'))
        bookmark_type = ContentType.objects.get_for_model(Details)
        #test = ' | '.join([x.label for x in Details.objects.filter(object_id=page_section.id)])
        test = ' | '.join([x.label for x in all])
        #print(test)
        #print(Details(content_object=self))
        return test + t_sereis
    
admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(PageSection, PageSectionAdmin)
# admin.site.register(PageSection, PageSectionAdmin)
