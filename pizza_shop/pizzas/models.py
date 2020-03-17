from django.db import models
# Create your models here.
class Pizza(models.Model):
    """ 创建Pizza数据表 """
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Topping(models.Model):
    """ 创建Topping数据表 """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
