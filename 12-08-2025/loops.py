# what is a loop?
# a loop is basically a way to repeat a block of code multiple times until a certain condition is met

# in python there are 2 types of loops
# 1. while loop
# 2. for loop


# for loop

# numbers = [1,2,3,6,5,7,89,2,5,8,2,5,9,,2,2...................100 elements]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])

# for loop and while loop

# for loop --> iterates over a sequence (list, tuple, string) or collection (dictionary, set, frozenset) and executes a block of code for each item in the sequence


# general syntax of for loop
# for x in list1:
# statement1
# statement2
# statement3

# list1 = [1, 55, 333, 88, 23, 56, 6]

# for i in list1:
#     print(i, end=" ")

# 1st iteration  , i = 1, 2
# 2nd iteration, i = 55, 110
# 3 rd iteration, i = 333, 666


# for i in (4,2,3,5):
#     print(i,end="")

# for i in sequence --> list, tuple, string etc.tuple
# for i in range
# for i in enumerate
# for i in zip

# range() --> generates number 
# syntax --> range(start,stop,step)

# for i in range(200,100,-1):
#     print(i)

# for i in range(1,3): #outer for loop
#     print("Table of",i)
#     for j in range(1,4): #inner for loop
#         print(i,"X",j,"=",i*j)
    
# outer loop --> i = 1 , "Table of 1"  #inner loop --> 1X1=1
                          #inner loop --> 1x2 = 2
                          #inner loop --> 1x3 = 3
                          
# outer loop --> i = 2 , "Table of 2"  #inner loop --> 2X1=2
                          #inner loop --> 2x2 = 4
                          #inner loop --> 2x3 = 6
                    
# list2 = [4,5,6,8,9,6]                         
# for i in list2:
#     print(i)
#     if i == 6:
#         break
    
    
# loop contorl statements
# break, continue and pass


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# example basic coding question

# write a function sum_number(n) that use for loop to calculate sum of numbers from 1 to n

# sum_number(5) --> 1+2+3+4+5
# sum_number(6) --> 1+2+3+4+5+6
# def sum_number(n):
#     sum = 0 #1 ,3 ,  6
#     for i in range(1,n+1): #(3+1=4)  #1, 2, 3,
#         sum = sum + i 
#     print(sum)

# sum_number(3)

# write a function to calculate the sum of even numbers from 1 to n

# def sum_even_numbers(n):
#     sum = 0
#     for i in range(2,n+1,2):
#         sum = sum + i   
#     print(sum)
  
# sum_even_numbers(5) # 2 + 4 + 6 + 8 => 20

# write a function print_table(num) that prints the multiplication table of num


# def print_table(num):
#     for i in range(1,11):
#         print(num,"X",i,"=",num*i)
    
        
# print_table(1024)


# wrtie a function count_vowels(word) that counts how many vowels are in the word
# def count_vowels(word):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for i in word:
#         if i in vowels:
#             count = count + 1
#     print(count)        
       

# count_vowels("cauliflower")
    
    



# list squares
# write a function that takes a list of numbers and returns a list of the squares of those numbers

# def list_squares(list1):
#     list2 = []
#     for i in list1:
#         list2.append(i*i)
#     print(list2)
   
# list_squares([2,5,6,7,8]) # --> [4,25,36,49,64]  

# def reverse_String(str):
#     rev_String = ""  #p+""  = p, y+p = yp,  t + yp = typ, so on 
#     for i in str:
#         rev_String = i + rev_String     
#     print(rev_String)
   
# reverse_String("python") #--> nohtyp 
#1st iteration i = p

# x = (1,2,3,6,9,80)

# print(len(x))

# words_lenght(["apple","banana","cherry"]) --> apple : 5, banana: 6, cherry: 6


# loops conditional statement
# break 
# continue
# pass

# for i in range(10):
#     if i == 6:
#         pass
#     print(i)

# while loop
# while condition:
#     statement1
#     statement2
#     statement3
#     statement4
    

# basic loop example
# count = 1
# while count <= 5:
    
#     if count == 3:
#         break
#     print(count)
#     count+=1
    
#2nd iteration  ==> 2 
#3rd iteratoion ==> count 3
# 4th iteration ==> count 4
# 5 th iteration ==> count 5
# before 6th iteration ==> count 6


#else clause in loops
# python allows an else with loops

# for i in range(5):
#     if i == 3: 
#         break
#     print(i)
# else:
#     print("loops finished suucessfully")