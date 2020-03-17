import sys
import os
import django

# 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')
django.setup()

from pizzas.models import Pizza
pizzas=Pizza.objects.all()
for pizza in pizzas:
    print(pizza.id, pizza.name)
print(pizzas)
t = Pizza.objects.get(id=5)
print(t.name)
print(t.topping_set.all())