from datetime import datetime

import xadmin
from .models import ShoppingCart,OrderInfo,OrderGoods



class ShoppingCartAdmin(object):
    list_display = ['name','goods','nums',]

class OrderInfoAdmin(object):
    list_display = ['user','order_sn','nonce_str','trade_no','pay_status','post_script',
                    'order_mount','order_mount','pay_time','add_time']

    class OrderGoodsInline(object):
        models = OrderGoods
        exclude = ['add_time',]
        extra = 1
        style = 'tab'

    inline = [OrderGoodsInline,]

xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)