while True:
    print('who are you?')
    name = input('>')
    if name != 'Bob':
        continue
    print('Hello, Bob. What is the password?(it is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted')
