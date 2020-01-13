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
