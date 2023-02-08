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
print('Logo', logo.image.url)
def test(request):
    template_name = 'frontend/test.html'
    url = 'http://127.0.0.1:8001/products/varientlist/'
    api = requests.get(url=url)
    print(api)
    context = {
        'api':list((api.json()))
    }
    return render(request, template_name, context)

def products(request):
    template_name = 'frontend/pages/products/products.html'
    context = {
        'logo': logo,
        'header': header,
    }
    return render(request, template_name, context)
def home(request):
    template_name = 'frontend/pages/home/home.html'
    #template_name = 'frontend/test.html'
    # page = PageCategory.objects.select_related('allPageSection', 'allPageSection__sectionText', 'allPageSection__sectionImage', 'allPageSection__carousel').filter(name='home').first()
    page = PageCategory.objects.filter(name='home').first()
    section1 = page.allPageSection.all().filter(name='section1').first()
    section2 = page.allPageSection.all().filter(name='section2').first()
    section3 = page.allPageSection.all().filter(name='section3').first()
    section4 = page.allPageSection.all().filter(name='section4').first()
    section5 = page.allPageSection.all().filter(name='section5').first()
   
    #page = PageCategory.objects.filter(name='home').first()
    products = Products.objects.all()
    logo = header.sectionImage.all().first()
    
    context = {
        'logo': logo,# logo
        'header': header,
        'page': page,
        'section1': section1,
        'section2': section2,
        'section3': section3,
        'section4': section4,
        'section5': section5,
        'products': products,
    }
    return render(request, template_name, context)
