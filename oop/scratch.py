class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# class Dog:
#     species = 'Canis familiaris'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# miles = Dog('Miles', 4)
# buddy = Dog('Buddy', 9)
# print(miles.name)
# print(buddy.age)
# buddy.age = 10
# print(buddy.age)
# print(buddy.species)

####Instances

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    #Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    #Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}!"
    
    
class JackRussellTerrier(Dog):
    def speak(self, sound='Arf'):
        return super().speak(sound)
        #return f"{self.name} says {sound}!"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
arnie = GoldenRetriever('Arnie', 3)

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
print(miles.speak('Grr'))
print(jim.speak('Woof'))
print(arnie.speak())


# print(miles.species)
# print(type(jack))
# print(isinstance(miles, Dog))
# print(isinstance(miles, Bulldog))
# print(isinstance(jack, Bulldog))

# print(miles.speak('Woof'))
# print(miles.speak('Bow wow ;)'))
# print(miles)

# Exercise - create car class

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage

#     def __str__(self):
#         return f"The {self.color} has {self.mileage} miles"
    

# blue = Car('blue', '20,000')
# red = Car('red', '30,000')
# print(blue)
# print(red)


# Inheritance

class Parent:
    speaks = ['English']

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks = Parent.speaks + ["German"]

# Inheritance - scroll back up to dog