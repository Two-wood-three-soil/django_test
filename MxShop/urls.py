"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include,re_path
from django.views.static import serve
import xadmin


from goods.view_base import GoodsListView
from goods.views import GoodsListViewSet,CategoryViewSet

from MxShop.settings import MEDIA_ROOT
router = DefaultRouter()

#配置goods的urls
router.register(r'goods',GoodsListViewSet)
#配置Category的url
router.register(r'categorys',CategoryViewSet,base_name="categorys")
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
     # 富文本编辑器url
    path('ueditor/', include('DjangoUeditor.DjangoUeditor.urls')),
    # path('goods/',GoodsListView.as_view(),name='goods-list'),
    path('docs',include_docs_urls(title="三土")),
    path('api-auth',include('rest_framework.urls')),
    re_path('^',include(router.urls)),
#文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # 首页
    # path('index/', TemplateView.as_view(template_name='index.html'), name='index'),

]
