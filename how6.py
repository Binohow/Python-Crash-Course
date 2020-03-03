""" capter-6 字典"""
# %%
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
print(alien_0["color"])
print(alien_0["point"])
alien_0['x'] = 5
alien_0['y'] = 6
print(alien_0["x"])
print(alien_0["y"])
# %%
# 先创建一个空字典
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 5
print(alien_1)
alien_1['points'] = 200
print(alien_1)
del alien_1['points']
print(alien_1)
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'endward': 'ruby',
    'phil': 'python'
}
print(favorite_languages)
# A:a, A是主键
for person in favorite_languages:
    print(person)
    print(person+' '+favorite_languages[person])
for name, languages in favorite_languages.items():
    print(name.title()+"'s favorite language is" + languages.title() + ".")
for name in favorite_languages.keys():
    print(name.title())
for name in sorted(favorite_languages.keys()):
    print(name.title())
# %%

# %%
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    print(alien_number)
for alien in aliens[:5]:
    print(alien)
print('...')

print("Total number of aliens: "+str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in alien[0:5]:
    print(alien)
# %%
how = {
    'how1': 1,
    'how2': 2,
    'how3': 3,
    'how456': [4, 5, 6]
}
print(how)

for hhow, number in how.items():
    print(hhow.title())
    print(number)
# %%
user = {
    'how1': {
        'first': 'bin1',
        'last': 'how',
        'location': 'princetion'
    },
    'how2': {
        'first': 'bin1',
        'last': 'how',
        'location': 'princetion'
    }
}

for username, user_info in user.items():
    print("\nUsername "+username)
    full_name = user_info['first'] + user_info['last']
    print("\nfull_name "+full_name)
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# %%
