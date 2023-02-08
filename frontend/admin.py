from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import(
    PageCategory,
    Carsoul,
    SectionText,
    SectionImage,
    PageSection
)
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
    inlines = [
        PageSectionInline,
    ]
class PageSectionAdmin(admin.ModelAdmin):
    list_filter = ('pageCategory__name',)
    
    inlines = [
        CarsoulInline,
        SectionTextInline,
        SectionImageInline,
    ]
    
admin.site.register(PageCategory, PageCategoryAdmin)
admin.site.register(PageSection, PageSectionAdmin)
# admin.site.register(PageSection, PageSectionAdmin)
