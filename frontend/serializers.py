from rest_framework import serializers
from product.models import Category
from .models import PageCategory

class PageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PageCategory
        #fields = ['id', 'name', 'text']
        fields = ('__all__')

    