from django.views.generic import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        #通過django的view实现商品列表页
        json_list = []
        #获取所有的商品
        goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
            #获取每个字段的值
            # json_dict['name'] = good.name
            # json_dict['category'] = good.category.name
            # json_dict['market_price'] = good.market_price
            # json_list.append(json_dict)

        from django.http import JsonResponse,HttpResponse
        from django.forms.models import model_to_dict
        from django.core import serializers
        import json
        #返回json，一定要指定类型content_type='application/json'
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list),content_type='application/json')
        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)

