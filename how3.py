how = ['how1', 'how2', 'how3']
for hower in how:
    print(hower)
even_number = list(range(2, 11, 2))
print(even_number)
squres = []
for value in range(1, 11):
    squre = value**2
    squres.append(squre)
print(squre)
# %%
for value in range(1, 21):
    print(value)
# %%
cubes = [value*value*value for value in range(1, 11)]
print(cubes)
# %%
list1 = list(range(1, 11))
print(list1[0:3])
print(list1[-2:])
# %%
hows = ['how1', 'how2', 'how3']
for how in hows[:2]:
    print(how)

howss = hows[:]
hows.append('how4')
howss.append('how5')
print(howss)
print(hows)

# %%
