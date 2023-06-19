from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title','products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description','slug','inventory' , 'unit_price', 'price_with_tax', 'collection' ]
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #1st method
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset= Collection.objects.all()
    # )
    #2 method
    # collection = serializers.StringRelatedField()
    #3 method
    #collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection_detail'
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)