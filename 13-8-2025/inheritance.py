# parent class and child 

# class ParentClass:
#     pass

# class ChildClass(ParentClass):
#     pass

# types of inheritance in pytohn
# single level inheirtance
# multilevel level inheritsnce
# multiple inheritance
#  mro --> method resolution order


class Grandfather:
    def __init__(self):
        self.hobby = "Reading News Paper"
    def speak(self):
        print("humble and polite")
    def property(self):
        print("15 kile gaon mein")
        
class Father(Grandfather):
    def speak(self):
        print("Aggressive and not polite")
class Mother:
    pass
class Boy(Father,Mother):
    def passion(self):
        print("Always in lethargic state")

class Girl(Father,Mother):
    pass 
 
# gf = Grandfather()
# print(gf.hobby)
ft = Father()

ft.speak()
ft.property()



# c1 = Child()
# print(c1.hobby)


class Father:
    # def __init__(self):
    #     self.property = "2 Flats Noida mein"
    def property(self):
        print("2 Flats Noida mein")
    def location(self):
        print("Noida","Father")
        
class Mother:
    def nature(self):
        print("polite and caring")
    def location(self):
        print("Noida", "mother")

class Child(Mother, Father):
   pass

c1  = Child()
# c1.location()

# print(c1.mro())   


