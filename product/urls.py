from django.urls import path, include
from . import views
app_name= 'product'
urlpatterns = [
    path('iphone/', views.category, name='category'),
    path('samsung-phones/', views.category, name='category'),
    path("iphone/<slug:slug>/", views.categoryDetail, name="categoryDetail"),
    path("iphone/<slug:slug>/<slug:s_slug>/", views.series, name="series"),
    path("iphone/<slug:slug>/<slug:s_slug>/<slug:m_slug>/", views.phoneModels, name="phoneModels"),
    path("iphone/<slug:slug>/<slug:s_slug>/<slug:m_slug>/<slug:p_slug>/", views.products, name="products"),
]

