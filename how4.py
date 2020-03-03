# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
""" 打印消息“Three items from the middle of the list are:”，再使用切
片来打印列表中间的三个元素。 """
how = 'Three items from the middle of the list are:'
M = len(how) / 2
if float.is_integer(M):
    print('是')
else:
    print('否')
print(M)
