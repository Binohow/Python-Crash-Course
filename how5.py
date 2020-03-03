""" if语句 """
# %%
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)
# %%
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# %%
x = True
y = False
# %%
age = input("Enter your age:")
age = int(age)
if(age >= 18):
    print("you can")
else:
    print("you can't")

# %%
how = ['how1', 'how2', 'how3']
# %%
age = input("Enter your age:")
age = int(age)
if age > 10:
    print(age)
elif age > 20:
    print(age)
elif age > 30:
    print(age)
else:
    print(age)
# %%
how = ['how1', 'how2', 'how3']
for myhow in how:
    newstr = myhow+"coder"
    if myhow == 'how1':
        print(newstr)
    else:
        print(myhow)
how.clear()
len(how)
# %%
nums = range(1, 10)
for num in nums:
    if num == 1:
        print(str(num)+'st')
    elif num == 2:
        print(str(num)+'nd')
    elif num == 3:
        print(str(num)+'nd')
    else:
        print(str(num)+'th')

# %%
