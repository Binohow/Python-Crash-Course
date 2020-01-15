""" capter-3 """
""" 学习列表操作 """
motorcycles = ['honda', 'yamaha', 'suzuki']
""" 输出列表元素 """
print(motorcycles)
""" 修改链表元素 """
motorcycles[0] = 12346
print(motorcycles[0])
""" 链表元素添加 """
# 末尾添加
motorcycles.append(456789)
print(motorcycles)
""" 在列表中插入元素 """
motorcycles.insert(2, 'howbin')
print(motorcycles)
motorcycles.pop(2)
print(motorcycles)
motorcycles.append(456789)
print(motorcycles)
motorcycles.remove(456789)
print(motorcycles)
""" 倒着打印列表 """
# 使用方法sort() 对列表进行永久性排序
""" motorcycles.sort()
print(motorcycles) """
# 使用函数sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars, reverse=True))
# 倒着打印列表
# print(cars.reverse()) 这样的方式将会输出 none值
cars.reverse()
print(cars)
# 确定列表的长度
print(len(cars))
""" 3.4使用列表时避免索引错误 """
# 注意-1使列表最后一个元素
print(cars[-1])
