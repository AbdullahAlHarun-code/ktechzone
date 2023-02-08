from django.shortcuts import render
from .models import (
    Category, 
    CategoryImage,
    Series,
    PhoneModel,
    Products,
    ProductVariation
    )
from django.shortcuts import get_object_or_404
# Create your views here.

def category(request):
    template_name = 'product/category/category.html'
    context = {
        'category': Category.objects.all()
    }
    return render(request, template_name, context)

def categoryDetail(request, slug):
    template_name = 'product/category/categoryDetail.html'
    categoryDetails = get_object_or_404(Category, slug=slug)
    print(categoryDetails)
    context = {
        'categoryDetails': categoryDetails
    }
    return render(request, template_name, context)

def series(request, slug, s_slug):
    template_name = 'product/category/series.html'
    seriesDetails = get_object_or_404(Series, slug=s_slug)
    context = {
        'seriesDetails': seriesDetails
    }
    return render(request, template_name, context)

def phoneModels(request, slug, s_slug, m_slug):
    template_name = 'product/category/models.html'
    phoneModelDetails = get_object_or_404(PhoneModel, slug=m_slug)
    context = {
        'phoneModelDetails': phoneModelDetails
    }
    return render(request, template_name, context)


def products(request, slug, s_slug, m_slug, p_slug):
    if request.method=='POST':
        field_name=(request.POST.get('detect_button'))
        p_slug = request.POST.get(field_name)
    else:
        field_name = 'capacity'
    template_name = 'product/items/products-details.html'
    productsDetails = get_object_or_404(Products, variation__slug=p_slug)
    productsDetailsVariation = get_object_or_404(ProductVariation, slug=p_slug)
    if field_name == 'capacity': selectValue = ProductVariation.objects.filter(**{field_name: productsDetailsVariation.capacity})
    if field_name == 'color': selectValue = ProductVariation.objects.filter(**{field_name: productsDetailsVariation.color})
    if field_name == 'conditions': selectValue = ProductVariation.objects.filter(**{field_name: productsDetailsVariation.conditions})
    product_slug = p_slug.split('-')
    print(product_slug)
    for slug in product_slug:
        if 'gb' in slug:
            print(slug)

    context = {
        'productsDetails': productsDetails,
        'productsDetailsVariation':productsDetailsVariation,
        'selectValue':selectValue
    }
    return render(request, template_name, context)
