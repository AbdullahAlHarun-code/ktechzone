
from django.urls import path, include
from . import views as frontViews
from account import views as accountViews
from product import views as productViews
from cart import views as cartViews
from checkout import views as checkoutViews
from .views import *
urlpatterns = [
    # front all pages url 
    path('', home, name='home'),
    # path('about-us/', frontViews.aboutUs, name='aboutUs'),
    # path('terms-condition/', frontViews.termsConditions, name='termsConditions'),
    # path('contact-us/', frontViews.contactUs, name='contactUs'),
    # path('reviews/', frontViews.reviews, name='reviews'),

    # # account url
    # path('account/login/', accountViews.login, name='login'),
    # path('account/register/', accountViews.register, name='register'),
    # path('account/logout/', accountViews.logout, name='logout'),
    # path('account/forget-password/', accountViews.logout, name='logout'),
    # path('account/success-pasword/', accountViews.logout, name='logout'),
    # path('account/active-account/', accountViews.logout, name='logout'),


    # path('account/dashboard/', accountViews.dashboard, name='dashboard'),
    # path('account/orders/', accountViews.orders, name='orders'),
    # path('account/address/', accountViews.address, name='address'),
    # path('account/profile/', accountViews.login, name='login'),
    # path('account/wishlist/', accountViews.login, name='login'),

    # # cart 
    # path('cart/', frontViews.cart, name='cart'),
    # path('compare/', frontViews.reviews, name='reviews'),

    # # checkout
    # path('checkout/', checkoutViews.checkout, name='checkout'),
    # path('order/', checkoutViews.order, name='order'),
    # path('success/', checkoutViews.success, name='success'),
    # path('cancel/', checkoutViews.cancel, name='cancel'),

    # # for help url 
    # path('help/', frontViews.help, name='help'),
    # path('help/delivery/', frontViews.helpDelivery, name='helpDelivery'),
    # path('help/return/', frontViews.helpReturn, name='helpReturn'),
    # path('help/payment-methods/', frontViews.helpPaymentMethod, name='helpPaymentMethod'),
    # path('help/get-price-query', frontViews.helpGetPriceQuery, name='helpGetPriceQuery'),

    # # collections 
    # path('collections/iphones/', productViews.iphones, name='iphones'),
    # path('collections/samsung-phones/', productViews.samsung, name='help'),
    # path('collections/tablets/', productViews.tablets, name='tablets'),
    # path('collections/ipads/', productViews.ipads, name='ipads'),
    # path('collections/headphones/', productViews.help, name='help'),
    # path('collections/laptops/', productViews.help, name='help'),
    # path('collections/case-temp/', productViews.help, name='help'),
    # path('collections/chargers/', productViews.help, name='help'),
    # path('collections/smartwatches/', productViews.help, name='help'),
    # path('collections/monitors/', productViews.help, name='help'),
]
