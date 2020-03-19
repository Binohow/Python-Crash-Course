from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有pizzas
    re_path(r'^pizzas/$', views.pizzas, name='pizzas'),
    # 显示特定的pizza页面，显示他的配料
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    #re_path(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza')
    # 用于添加新主题的网页
    path('new_pizza/', views.new_pizza, name='new_pizza')
]
app_name = 'pizzas'
