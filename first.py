# Type function
# CAT1= 30
# CATT2 = 25
# EXAM = 50
# E_CAT = (CAT1 + CATT2)/2
# Checking what datatype is CAT1
# print(type(CAT1))
#string conversions
# age = 11
# Age = float(age)
# print(Age)
#user input
# name = input("Whats your name: ?")
# print('welcome',name)
#conditional statements
# x = input("enter a number")
# X =int(x)
# if X < 5:
#     print("smaller than 5")
# if X  > 5:
#     print("greater than 5")
# print(X)
# try / except
# astr = 'hello bob'
# try:
#     istr = int(astr)
# except Exception as e:
#     warning ="something went wrong"
#     print(warning)

# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('second', istr)


#  functions in python
# x = 5
# def print_lyrics():
#     print("I am benson")
#     print('benson the good guy')
    
# print('youuuuh')
# print_lyrics()
# x= x+2
# print(x)
# lang =input("enter language initials: ")
# def greet(lang):
#     if lang == 'es':
#         print("Holla")
#     elif lang== 'fr':
#         print('Bonjor')
#     else:
#         print("hello")
        
# greet(lang)


#Return statement
# python doesnt execute the next line after meeting return function
# x1 = int(input("Enter the first value: "))
# y2= int(input("Enter the second value: "))
# def sum(x,y):
#     if x > y :
#         return 'x is larger'
#     elif y > x:
#         return 'y is greater'
#     else:
#         return 'i am confused'
    
# print(sum(x1,y2))


# Loops and Iterations
# Indefinite loops.
# They are called indefinite since they run until some
# logical condition becomes false.

# n = 500
# while n > 0:
#     print(n)
#     n = n-1
#     # print(n)

# breaking out of a loop
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done')

# continue statement
# while True:
#     line = input("> ")
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print("Very Done")


# Definite Loops