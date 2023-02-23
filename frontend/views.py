from django.shortcuts import render
from .serializers import PageCategorySerializer
import requests
import json
from product.models import Products
from .models import(
    PageCategory,
    Carsoul,
    SectionText,
    SectionImage,
    PageSection
)
# Create your views here.
base = PageCategory.objects.filter(name='base').first()
header = base.allPageSection.filter(name='header').first()
logo = header.sectionImage.all().first()
def test(request):
    template_name = 'frontend/test.html'
    url = 'http://127.0.0.1:8001/products/varientlist/'
    url1 = 'http://127.0.0.1:8002/collections/'
    api = requests.get(url=url)
    api1 = requests.get(url=url1)
    print(api)
    context = {
        'api':list((api.json())),
        'api1':list((api1.json()))
    }
    return render(request, template_name, context)

def products(request):
    template_name = 'frontend/pages/products/products.html'
    context = {
        'logo': logo,
        'header': header,
    }
    return render(request, template_name, context)
def basic_info():
    pass
def all_products(request,slug=None, sub_slug=None):
    template_name = 'frontend/pages/products/products.html'
    api_url = 'http://127.0.0.1:8002/'
    if slug is not None and sub_slug is None:
        url1 = f'http://127.0.0.1:8002/products/{slug}'
    elif slug is not None and sub_slug is not None:
        
        url1 = f'http://127.0.0.1:8002/products/{slug}/{sub_slug}'
    else:
        url1 = 'http://127.0.0.1:8002/products/'
    url2 = 'http://127.0.0.1:8002/collections/'
    #api = requests.get(url=url)
    products = requests.get(url=url1)
    api1 = requests.get(url=url2)

    page = PageCategory.objects.filter(name='products').first()
    header = page.allPageSection.all().filter(name='header').first()
    
    context = {
        'header':header,
        'logo': logo,# logo
        'products':list((products.json())),
        'api1':list((api1.json())),
        'api_url':api_url,
    }
    return render(request, template_name, context)
def home(request):
    template_name = 'frontend/pages/home/home.html'
    url = 'http://127.0.0.1:8001/products/varientlist/'
    url1 = 'http://127.0.0.1:8002/collections/'
    #api = requests.get(url=url)
    api1 = requests.get(url=url1)
    #template_name = 'frontend/test.html'
    # page = PageCategory.objects.select_related('allPageSection', 'allPageSection__sectionText', 'allPageSection__sectionImage', 'allPageSection__carousel').filter(name='home').first()
    page = PageCategory.objects.filter(name='home').first()
    print('Category Test', page.tags.all())
    section1 = page.allPageSection.all().filter(name='section1').first()
    section2 = page.allPageSection.all().filter(name='section2').first()
    section3 = page.allPageSection.all().filter(name='section3').first()
    section4 = page.allPageSection.all().filter(name='section4').first()
    section5 = page.allPageSection.all().filter(name='section5').first()
   
    #page = PageCategory.objects.filter(name='home').first()
    products = Products.objects.all()
    logo = header.sectionImage.all().first()
    
    context = {
        'api1':list((api1.json())),
        'logo': logo,# logo
        'header': header,
        'page': page,
        'section1': section1,
        'section2': section2,
        'section3': section3,
        'section4': section4,
        'section5': section5,
        'products': products,
        'test': 45,
    }
    return render(request, template_name, context)
