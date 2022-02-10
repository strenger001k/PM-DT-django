from rest_framework import serializers
from .models import Сategory, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'scope',
                  'diameter',
                  'length',
                  'color',
                  'get_pic',)


class CardSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Сategory
        fields = ('id', 'name', 'products',)


class SubGroupSerializer(serializers.ModelSerializer):
    children = CardSerializer(many=True, required=False)
    class Meta:
        model = Сategory
        fields = ('id', 'name', 'children',)


class GroupSerializer(serializers.ModelSerializer):
    children = SubGroupSerializer(many=True, required=False)
    class Meta:
        model = Сategory
        fields = ('id', 'name', 'children',)


class SectionSerializer(serializers.ModelSerializer):
    children = GroupSerializer(many=True, required=False)
    class Meta:
        model = Сategory
        fields = ('id', 'name', 'children',)


class СategorySerializer(serializers.ModelSerializer):
    children = SectionSerializer(many=True, required=False)
    class Meta:
        model = Сategory
        fields = ('id', 'name', 'description', 'children',)


class AllСategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сategory
        fields = ('name', 'description',)
