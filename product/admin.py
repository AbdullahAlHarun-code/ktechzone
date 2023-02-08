from django.contrib import admin
from product.models import (
    Category, 
    CategoryImage, 
    Series, 
    PhoneModel,
    Products,
    ProductImage,
    ProductVariation,
    Condition,
    Color,
    Capacity,
    Offer
    )
# Register your models here.
class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 0
class SeriesInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("name",)} 
    model = Series
    extra = 0

class ModelInline(admin.TabularInline):
    prepopulated_fields = {"slug": ("name",)} 
    model = PhoneModel
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
    inlines = [
        CategoryImageInline,
        SeriesInline
    ]
    
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
    inlines = [
        ModelInline
    ]

class ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
    search_fields = ['name']

class OffernInline(admin.TabularInline):
    model = Offer
    extra = 0

class ProductVariationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("capacity",'color', 'conditions', )} 
    inlines = [
        OffernInline,
    ]

class CategoryImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 0

class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
    autocomplete_fields = ['phoneModel']
    search_fields = ['phoneModel']
    inlines = [
        CategoryImageInline,
        ProductVariationInline,
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(PhoneModel, ModelAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Condition)
admin.site.register(Color)
admin.site.register(Capacity)
admin.site.register(Offer)
