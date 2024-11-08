#Cat entity
class Cat:
    #The constructor: creates an instance of a class
    #The constructor will create a cat for us in code
    #To create a cat, we need given_name and given_colour
    def __init__ (self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour

#An instance of Cat
#An instance is a specific occurrence of a class

mimi = Cat("Mimi", "Brown")
print(mimi.name)
print(mimi.colour)