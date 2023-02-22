from django.contrib import admin

# Register your models here.
from .models import(
    StoreCollection,
    Collection,
    SubCollection,
    SubSubCollection
)
class SubSubCollectionInline(admin.TabularInline):
    model = SubSubCollection
    extra = 0
class SubCollectionInline(admin.TabularInline):
    model = SubCollection
    extra = 0
class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 0

class StoreCollectionAdmin(admin.ModelAdmin):
    inlines = [
        CollectionInline,
    ]
    
class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        SubCollectionInline,
    ]
class SubCollectionAdmin(admin.ModelAdmin):
    inlines = [
        SubSubCollectionInline,
    ]
admin.site.register(StoreCollection, StoreCollectionAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(SubCollection, SubCollectionAdmin)
admin.site.register(SubSubCollection)