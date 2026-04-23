def hello(): #print 3 greetings
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')

hello()
hello()
print('Once more')
hello()


def say_hello_to(name):
    #Prints three greetings to the name
    print('Good morning, ' + name)
    print('Good afternoon, ' + name)
    print('Good evening, ' + name)

say_hello_to('Timmy')

# The call stack
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
a()


#Global vs local variables
def spam():
    global eggs
    eggs = 'spam' #global
def bacon():
    eggs = 'bacon' #local
def ham():
    print(eggs) # global
eggs = 'global' # global
spam()
print(eggs)

#error handling
def spam(divide_by):
    try:
        #any code in this block that causes ZeroDivisionError wont crash
        return 42 / divide_by
    except ZeroDivisionError:
        #It it happens, the code will then run this:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
