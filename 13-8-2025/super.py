# super() keyword is used to access method or varibale from a parent class
# without directly naming the parent class
# it supports multiple in heritance thorugh python mro

#super().method_name(arguments)

class Parent:
    def __init__(self,name):
        self.name = name
        print("Parent __init__ called")       
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print("child __init__ called")
obj = Child("Rahul",55)


