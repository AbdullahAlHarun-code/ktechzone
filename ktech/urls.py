from django.conf.urls.static import static 
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from frontend.views import *
import debug_toolbar 

urlpatterns = [
    path('admin/', admin.site.urls),
        
    path('', home, name='home'),
    path('products/', all_products, name='all_products'),

    # all phones url
    path('test/', test, name='test'),
    path('phones/', products, name='products'),
    path('phones/iphones/', home, name='home'),
    path('phones/iphones/<slug:slug>/', home, name='home'),
    path('phones/samsung-phones/', home, name='home'),
    path('phones/samsung-phones/<slug:slug>/', home, name='home'),
    path('phones/other-phones/', home, name='home'),
    path('phones/other-phones/<slug:slug>', home, name='home'),

    # all Accessories url
    path('accessories/', home, name='home'),
    path('accessories/cases/', home, name='home'),
    path('accessories/cases/<slug:slug>', home, name='home'),

    path('accessories/audio/', home, name='home'),
    path('accessories/audio/<slug:slug>', home, name='home'),

    path('accessories/chargers/', home, name='home'),
    path('accessories/chargers/<slug:slug>', home, name='home'),

    path('accessories/tempered-glass/', home, name='home'),
    path('accessories/tempered-glass/<slug:slug>', home, name='home'),

    path('accessories/gadgets/', home, name='home'),
    path('accessories/gadgets/<slug:slug>', home, name='home'),

    # All tablets url
    path('tablets/', home, name='home'),
    path('tablets/ipads/', home, name='home'),
    path('tablets/ipads/<slug:slug>/', home, name='home'),
    path('tablets/android-tablets/', home, name='home'),
    path('tablets/android-tablets/<slug:slug>/', home, name='home'),

    # All laptops url
    path('laptops/', home, name='home'),
    path('laptops/<slug:slug>/', home, name='home'),

    path('__debug__/', include('debug_toolbar.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL,   document_root=settings.MEDIA_ROOT)
