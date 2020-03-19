from django.shortcuts import render
from pizzas.models import  Pizza,Topping
from .forms import PizzaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    print(context)
    return render(request, 'pizzas\pizzas.html', context)

def pizza(request, pizza_id):
    """ 显示单个主题及其所有的条目 """
    print("pizza_id="+str(pizza_id))
    pizza = Pizza.objects.get(id=pizza_id)
    print("pizza="+str(pizza))
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings':toppings}
    print("context=")
    print(context)
    return render(request, 'pizzas\pizza.html', context)

def new_pizza(request):
    """ 添加pizza """
    print("request.method=")
    print(request.method)
    print(request)
    if request.method != 'POST':
       form = PizzaForm()
    else:
        # POST提交的数据,对数据进行处理
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pizzas:pizzas'))
    context = {'form': form}
    print("context=")
    print(form)
    return render(request, 'pizzas\my_new_pizza.html', context)
