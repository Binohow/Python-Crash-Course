""" capter-8 """
# %%


def greet_user(username):
    print("Hello"+username)


greet_user('Howbin')


# %%
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='harry', animal_type='hamster')
# %%


def describe_pet_1(animal_type='Dog', pet_name='dog'):
    """ 显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_1(pet_name='DDDog')


# %%
def get_formatted_name(first_name, last_name):
    " 返回完整的姓名 "
    full_name = first_name + last_name
    return full_name


full_name = get_formatted_name('how', 'bin')
print(full_name)
# %%


def get_formatted_name_1(first_name, last_name, middle_name=""):
    " 返回完整的姓名 "
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    return full_name


full_name = get_formatted_name_1('how', 'bin')
print(full_name)
full_name = get_formatted_name_1('how', 'bin', 'bin')
print(full_name)


# %%
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


person_1 = build_person('how', 'bin', '24')
person_2 = build_person('how2', 'bin2', '24')
persons = ['person_1', 'person_2']
for person in persons:
    myperson = {}
    exec("myperson = "+person)
    for key, value in myperson.items():
        print(key + ' ' + value)


# %%


def get_formatted_name_2(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name_2(f_name, l_name)
    print("\nHello, "+formatted_name+"!")


# %%
def greet_user2(names):
    """ 向列表中的每位用户都发出简单的问候 """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['how1', 'how2', 'how3']
greet_user2(usernames)


# %%
def print_models(unprintf_designs=[], complete_models=[]):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprintf_designs:
        current_design = unprintf_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model:"+current_design)
        complete_models.append(current_design)


def show_completed_models(complete_models=[]):
    """ 显示打印好的所有模型 """
    print("\nThe following models have been printed:")
    for complete_model in complete_models:
        print(complete_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# %%
def make_pizza(*toppings):
    for topping in toppings:
        print("-" + topping)


make_pizza("how1", "how2", "how3")
make_pizza("how1")


# %%
def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


use_profile = build_profile("how", "bin", how1="how2", how3="how4")
print(use_profile)

# %%
