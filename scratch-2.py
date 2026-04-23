#conditionals
username = 'Mary'
password = 'swordfish'
if username == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password')


#elif
name = 'Alice'
age = 33
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')


# Prints hello if 1 is stored in spam, howdy if 2, Greetings! if anything else
spam = int(input('Enter a number:>>>'))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


