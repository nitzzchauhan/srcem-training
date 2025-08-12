# what are opertors in python?

# they are special symbol that performs some operation on variables and values
# example

# print(5-3)
# print(5*3)
# print(5/3)
# print(5%3)
# print(5**3)
# print(5//3)

# types of operator in python
# arithmetic operator (+,-,/,**,%,//)
# assignment operator (=,+=,-=,*=,/=,%=)
# comparison operator (==,!=,>,<,>=,<=)
# logical operator (and,or,not)
# identity operator  (is,is not)
# membership operator  (in,not in)

# print(10/2)
# print(10//2) #floor division

# print(5%2) #modulus (remainder)
# print(10**2) #exponentiation
# print(10**3) #exponentiation
# print(2**3) #exponentiation

# comparison operator
# =  --> assignment operator
# print(10==10)
# print(10!=10) #--> not
# print(10>10)
# print(10<10)
# print(10>=10)
# print(10<=10)

# assignment operator

x = 5

# x = x+3
x+=3
x-=3  # x = x-3
x*=3  # x = x*3
x//=3  # x = x/3

# print(x)

#logical operators
# and

# condition1 and condition2 and condition3 and condition4 --> true
x = 10
y = 20

# print(x==10 and y > 15 and x < 5)
# (true and true) --> true

# true and false --> false

# or
# x = False
# y = False
# print(x or y)

# a  = True
# print(not not not a)

# membership operator
# in --> checks whether if a value is present in an sequence
# not in

# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)
# print("kiwi" not in fruits)
# print("kiwi" not in fruits)

# identity operartor
# is --> checks whether both the variables are same or not
# is not

x = 10
y = 10

print(x is y)
print(x is not y)