from django.shortcuts import render
from pizzas.models import  Pizza
# Create your views here.
def index(request):
    """ 学习笔记主页 """
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """ 显示所有 pizzas """
    pizzas = Pizza.objects.order_by('id')
    print("+++++")
    print("1+2")
    context = {'pizzas': pizzas}
    print(context)
    return render(request, 'pizzas\pizzas.html', context)
