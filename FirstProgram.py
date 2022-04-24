# print("Hello Coders")
#<----------------------------------------------------------------------------->
#Variables

# name = "Apurva"
# age = 20
# name = "Anuja"
# age = 15
# is_adult = True
# print(name)
# print(age)

#Ex 1
# first_name = "Tony"
# last_name = "Stark"
# age = 52
# is_genius = True
#<------------------------------------------------------------------------------->
#User input
# name = input("What is your name?")
# print("Hello" + name)

#Ex 2
# superhero = input("What is your Super Hero name?")
# print(superhero)
#<---------------------------------------------------------------------------------->
#Type Conversion
# old_age = input("What is your old age?")
# new_age = old_age + 2
# print(new_age)
#TypeError: can only concatenate str (not "int") to str

# old_age = input("What is your old age?")
# new_age = int(old_age) + 2
# print(new_age)

# number = 18
#print(float(number))
#<------------------------------------------------------------------------------------->

#Program to print the addition of 2 nos..

# first_num = input("Enter first number: ")
# sec_num = input("Enter second number: ")

# sum = first_num + sec_num
# print(sum)   # .....concatenation will occur

# sum = int(first_num) + int(sec_num)

# # print("The addition is: " + sum)
# # TypeError: can only concatenate str (not "int") to str
# print("The addition is: " + str(sum))

#<--------------------------------------------------------------------------------->

#Srings

# name = "Tony Stark"
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.find('S')) # returns the index of the occurance of character

# print(name.replace("Tony Stark", "Iron Man"))
# print(name)
# print(name.replace(" Stark", "Iron Man"))
# print(name.replace("T","M"))

# # To just check whether the substring exists or not...returns boolean value
# name = "Apurva Pawar"
# print("Apurva" in name)
# print("Sakshi" in name)
# print("P" in name)

#<----------------------------------------------------------------------------------->

#Arithmetic Operators

# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5//2)# does not show values after decimal point
# print(5%2)
# print(5**2)#raised to power

# i=5
# i= i+2
# i+=2
# i-=2
# i*=2
# i/=2
#<--------------------------------------------------------------------------------->

# #Operator precedence
# result = 2 + 3 * 5
# #PEDMAS rule is applied...

#<--------------------------------------------------------------------------------->

# Comparison Operators    .....return boolean values
# print(3>2)
#<------------------------------------------------------------------------------->

#Logical Operators  (3)
#1 or  2) and  3) not

#<------------------------------------------------------------------------------>

#If else statements

# age = 19
# age = int(input("What is your age?"))
# if age >= 18:
#     print("You are Adult")
#     print("You can vote")
# elif age < 18 and age >= 3:
#     print("you are in School")
# else:
#     print("you are a child")
       
# print("Thankyou")    
#<------------------------------------------------------------------------->
# #Building a Calculator

# first_num = int(input("Enter first number: "))
# operator = input("Enter operator(+,-,*,/,%):")
# sec_num = int(input("Enter second number: "))

# if operator == '+':
#     print(first_num + sec_num)
    
# elif operator == '-':
#     print(first_num - sec_num)
    
# elif operator == '*':
#     print(first_num * sec_num)       

# elif operator == '/':
#     print(first_num / sec_num)
    
# elif operator == '%':
#     print(first_num % sec_num)   
 
# else:
#     print("Invalid Operation!")     

#<-------------------------------------------------------------------------->
#Range ....ek number se dusre number tak jana
# numbers = range(5) #0,1,2,3,4
# print(numbers)

#<-------------------------------------------------------------------------->
#Loops

# #1. while loop
# i=1
# while i<=5:
#     print(i)
#     i+=5

# i=1
# while i <= 5:
#     print(i * "*")
#     i+=1
    
# i=5
# while i >=0:
#     print(i* "*")
#     i=i-1    
#______________________________________________________________________
# #2. For loops

# for i in range(5): #here i is any variable..
#     print(i+1)

#<------------------------------------------------------------------------------->
# # List   ....collection of items

# marks = [98,96,97]#"maths"]
# print(marks)
# #negative index  piche s ginti start karna
# print(marks[-1])
# print(marks[-2])
# print(marks[0:2])#prints only 0th and 1st index

# for score in marks:
#     print(score)

#_____________________________________________________________________
# #List Operations
# #1.append...kisi chij ko jod dena(last mai)

# marks = [95,96,97,98]
# marks.append(99)
# print(marks)
# #We use insert operation to add item/ele at btw position
# marks.insert(0,94)
# print(marks)

# # To check whether the element exist in the list or not
# print(99 in marks)#returns boolean value

# #Printing length of the list
# print(len(marks))#count starts from 1

# #Printing marks by while loop
# marks = [95,96,97,98]
# i=0
# while i < len(marks):
#     print(marks[i])
#     i=i+1

# #To clear the list
# marks = [95,96,97,98]
# marks.clear()
# print(marks)    
#<------------------------------------------------------------------------------------>

# # break and continue statements...

# students =  ["Appu","Anu","Anay","Sai","Jui","Sakshi","Aadi","Karan","Nini"]  

# for student in students:
#     if student == "Sai":
#         break;
#     print(student)  #Sai will not be printed here...only get printed till Anay
     
    
# students =  ["Appu","Anu","Anay","Sai","Jui","Sakshi","Aadi","Karan","Nini"]

# for student in students:
#     if student == "Jui":
#         continue;
#     print(student) # Only Jui will not be printed

#<--------------------------------------------------------------------------------->

# #Tuple....same as list but immutable...round brackets not compulsory..by default

# person = "ram","sham","raju"
# print(person)

# marks = (97,95,97,96,97)
# marks[0] = 99
# #TypeError: 'tuple' object does not support item assignment
# print(marks.count(97))  #3
# print(marks.index(97)) #returns index of first occurance of item

#<------------------------------------------------------------------------------------------>
# #Sets

# marks = {97,96,97,98,97}
# print(marks) #only unique values will come as output....97,96,98
# #In sets index does not exist....unordered

# for score in marks:
#     print(score)

#<---------------------------------------------------------------------------------------------->

# # Dictionary.....key value pair

# marks ={"English":95,"Chemistry":98}

# print(marks["Chemistry"])
# marks["Physics"] = 97;
# print(marks)

# marks["Physics"] = 99;
# print(marks)

#<----------------------------------------------------------------------------------------------------->

# # Functions
# def print_sum(first,sec=4):
#     print(first+sec)
    
# print_sum(1,2)   # print_sum(1)

#<----------------------------------------------DONE---------------------------------------->