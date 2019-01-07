from rest_framework import serializers
from .models import Goods,GoodsCategory

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

#ModelSerializer实现商品列表页

class CategorySerializer3(serializers.ModelSerializer):
    """三级分类"""

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    """二级分类"""
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """一级分类"""
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    #覆盖外检字段
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'
