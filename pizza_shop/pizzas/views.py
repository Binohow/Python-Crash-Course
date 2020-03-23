from django.shortcuts import render
from pizzas.models import  Pizza,Topping
from .forms import PizzaForm,ToppingForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    """ 学习笔记主页 """
    return render(request, 'pizzas/index.html')
@login_required
def pizzas(request):
    """ 显示所有 pizzas """
    pizzas = Pizza.objects.filter(owner=request.user).order_by('id')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas\pizzas.html', context)
@login_required
def pizza(request, pizza_id):
    """ 显示单个主题及其所有的条目 """
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404("Album does not exist")
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings':toppings}
    return render(request, 'pizzas\pizza.html', context)
@login_required
def new_pizza(request):
    """ 添加pizza """
    if request.method != 'POST':
       form = PizzaForm()
    else:
        # POST提交的数据,对数据进行处理
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            return HttpResponseRedirect(reverse('pizzas:pizzas'))
    context = {'form': form}
    return render(request, 'pizzas\my_new_pizza.html', context)
@login_required
def new_topping(request, pizza_id):
    """ 在特定的pizza中添加配料 """
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form =  ToppingForm()
    else:
        # POST提交的数据,对数据进行处理
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return HttpResponseRedirect(reverse('pizzas:pizza', args=[pizza_id]))
    context = {'pizza':pizza, 'form':form}
    return render(request, 'pizzas/new_topping.html', context)
@login_required
def edit_topping(request, topping_id):
    """ 编辑既有条目 """
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza
    if pizza.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = ToppingForm(instance=topping)
    else:
        # POST提交的数据，对数据进行处理
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pizzas:pizza', args=[pizza.id]))
    context = {'topping':topping, 'pizza':pizza, 'form':form}
    return render(request, "pizzas/edit_topping.html", context)
