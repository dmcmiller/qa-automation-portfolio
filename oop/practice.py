
# class Dog():
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} says Woof!")

# class GuideDog(Dog):
#     def __init__(self, name, breed, owner):
#         super().__init__(name, breed)
#         self.owner = owner

#     def bark(self):
#         print(f"{self.name} is working and cannot play right now")

#     def guide(self):
#         print(f"{self.name} is guiding {self.owner}")

    
# millie = Dog('Millie', 'Great Dane')
# bobby = Dog('Bobby', 'Golden Retriever')
# brown = GuideDog('Brown', 'German Shepherd', 'Mitchell')


# millie.bark()
# bobby.bark()
# brown.bark()
# brown.guide()


# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):         
#         return self.width * self.height
    
#     def describe(self):        
#         print(f"This rectangle is {self.width}x{self.height} with an area of {self.area()}")

# # test1 = Rectangle(5, 10)
# # print(test1.area())
# # test1.describe()

# r = Rectangle(5, 3)
# r.describe()



# def divide(a, b):
#     try:
#        return a / b
#     except ZeroDivisionError as error_mesg:
#         return(error_mesg)
#     finally:
#         print("Calculation attempted")

# print(divide(8, 2))
# print(divide(9, 0))
# print(divide(9, 2))