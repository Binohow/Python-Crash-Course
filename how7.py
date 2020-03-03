""" capter7 """
# %%
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

# %%
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
state = True
while state:
    message = input(prompt)
    if message == 'quit':
        state = False
    else:
        print(message)

# %%
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)


# %%
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num % 2 == 1:
        continue
    print(current_num)

# %%
x = 1
while x <= 5:
    print(x)
    x += 1
# %%
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()
    print("Verifying user: "+confirmed_user)
    confirmed_users.append(confirmed_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
# %%
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# %%
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + '.')

# %%


def greet_user():
    """ 显示简单的问候语 """
    print("Hello!")


greet_user()


# %%
