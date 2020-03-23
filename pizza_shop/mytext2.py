import sys
import os
import django

# 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')
django.setup()

from django.contrib.auth.models import User
from pizzas.models import Pizza

for user in User.objects.all():
    print(user.username, user.id)

for pizza in Pizza.objects.all():
    print(pizza.name+" " + str(pizza.owner))

