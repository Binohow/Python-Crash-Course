from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有问题
    re_path(r'^pizzas/$', views.pizzas, name='pizzas')
]
app_name = 'pizzas'
