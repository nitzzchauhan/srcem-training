# polymorphism --> many forms

# one name, many forms

# override #overloading(python doesnt support overloading)

# class Animal:
#     def speak(self):
#         return "Animal Speaks"  
# class Dog():
#     def speak(self): #overrided method
#         return "Woof"

# class Cat:
#     def speak(self):
#         return "meow"

# animals = [Dog(), Cat()]
# for i in animals:
#     print(i.speak())


# overloading
# not supported by the python

class Calculation:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
    def add(self,a,b,c=0,d=0):
        print(a+b+c+d)

c1 = Calculation()
c1.add(2,4)
        
        

    

        