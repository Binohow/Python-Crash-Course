# %%
from collections import OrderedDict


# %%
class Dog():
    """ 一次模拟小狗的简单尝试 """

    def __init__(self, name, age):
        """ 初始化属性name和age """
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗被命令时蹲下 """
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """ 模拟小狗被命令是打滚 """
        print(self.name.title() + "rolled over!")


mydog = Dog('while', 6)
mydog.sit()
mydog.roll_over()


# %%

class Car():
    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' +\
            self.model
        return long_name

    def read_odometer(self):
        """ 打印一条指出汽车里程的消息 """
        print("This car has " + str(self.odometer_reading) + " miles")

    def updata_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ 将里程表读数增加指定的量 """
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 55
my_new_car.read_odometer()
my_new_car.updata_odometer(0)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.updata_odometer(23500)
my_used_car.increment_odometer(500)

my_used_car.read_odometer()
# %%


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# %%


favorite_languages = OrderedDict()


favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name)
    print(language)
# %%

# %%

# %%
