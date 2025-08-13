# oops
# it is a paradigm that organises software design around objects

# objects -> layman terms --> real world entity is object
#         --> technically --> instance of an class


# key concepts of oops

# class
# objects(instances)
# attrubutes(properties)
# methods (function inside class) 
# pillar of python oops --> inheritance, encapsulation, abstraction, polymorphism

# classes and objects
# class --> blue printor template for creating objects
# .object -->
 
# general syntax of class

# class Classname:
    

# class Student:

#problem
    
# student1 = {"name":"rohan","age":17, "course":"MERN"}
# student2 = {"name":"amit","age":21, "course":"MERN"}
# student3 = {"name":"shahil","age":22, "course":"MERN"}
# student4 = {"name":"nidhi","age":23, "course":"MERN"}
#predefined classes
# str list tuple dict   
# template or class
class Student:
    #class variable
    location = "Noida"
    def __init__(self,name,age,course): #constructor will initialise and object and attach property to a objecy
        #instance variable
        self.name = name
        self.age = age
        self.course = course
        self.marks = [45,56,32]
    def __str__(self):
        
        return f"Student Name is: {self.name} and Student Age is: {self.age}"
    #methods
    
    def greet(self):
        print("Welcome",self.name) 
    def average(self):
        print(sum(self.marks)/3)
        
    # def setMarks(self):
    #     marks = input("Enter Marks")
    #     self.marks = [marks]
        
s1 = Student("Rohan",17,"MERN Stack")
s2 = Student("Rahul",55,"Politics")
s1.average()

# print(s1)
# print(s2)
# print(s1.name)
# print(s1.age)
# print(s1.course)
# print(s1.location)

# there are two main types of variables that
# you can have in a class
# class Variable
# Instance Variable
        
# x = ["mango","fruits","orange"]
# print(x)

# class XYZ:
    
#     def __init__(self, *args, **kwargs):
#         def __init__(*args, **kwargs):
#             pass
        
        # def __str__():
        #     return "[]"
        
        
# name = "Modi ji"

# print(f"lgkjegerjgioerig {name} {4+4}")
    