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
# for loop
# friends = ['Benson','Glen','Steve','Eve']
# for friend in friends:
#     print("Hello ", friend)
# print("Hellow World")


# find the largest number
# num = 0
# print("Before: ",num)
# for max_num in [1, 10,75,75,56,299,345,445]:
#     if max_num > num:
#             num = max_num
#             # print("The maximum number is",num)
# print("After The max number is: ", num)

# # counting in python
# zork = 0
# for num in [1,24,25,74,52,62,41,81,23,74,52,95]:
#     zork = zork +1
#     print(zork, num)
# print("After", zork)
# summing in a loop in python
# zork = 0
# print('Before', zork)
# for num in [1,24,25,74,52,62,41,81,23,79,52,95]:
#     zork = zork + num
#     print(zork, num)
# print("After", zork)

# # finding the smallest number
# smallest = None
# print('Before')
# for value in [1,24,25,74,52,62,41,81,23,79,52,95]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print("The smallest value is :", smallest)

# Strings
# # len function gives us the length of a string
# fruit = 'banana'
# fruit_length = len(fruit)
# print("The length of this string is:",fruit_length, "characters")

# looping through strings
# fruit = "banana"
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index +1


# looping through strings version 2
# fruit = "banana"
# for letter in fruit:
#     print(letter)


# #slicing strings
# name = "Benson Makau"
# print (name[0:4]) #prints the first character up to the fourth but not including the 4
# print (name[:4]) #starts from the first one
# print (name[2:]) #starts from the second up to the last
# print (name[:]) # starts from the first one to the last

# string concatinations\
# fname = "Benson"
# lname ="Makau"
# name = fname +" "+ lname
# print(name)

# Using in as a logical operator
# fruit = "Mango"
# if "a" in fruit:
#     print(fruit +" has letter a in its spelling")


#convert strings to lower case
# name = "Benson Makau"
# lower_case_name = name.lower()
# print(lower_case_name)

#convert strings to upper case
# name = "Benson Makau"
# upper_case_name = name.upper()
# print(upper_case_name)


# stuff = "Hello world"
# # new= type(stuff)
# new = dir(stuff)
# print(new)

# searching a string 
# fruit = "banana"
# pos = fruit.find("na")
# print(pos)

# search and replace
# name = "benson makau"
# new_name = name.replace('makau', 'mark')
# print(new_name )

# stripping white space
# greeting ="   Hello Genius  "
# print("no stripping functinality "+greeting)
# left_strip = greeting.lstrip()
# print("left stripping functinality "+ left_strip)
# right_strip = greeting.rstrip()
# print("right stripping functinality "+ right_strip)
# full_strip = greeting.strip()
# print("left and right stripping functinality "+ full_strip)

# prefixes
# line = "Please have a nice day"
# startswith = line.startswith('Please')
# startswith = line.startswith('P')
# print(startswith)

#READING FILES
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

#READING THE WHOLE FILE
# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
# #printing the first 20 characters
# print(inp[:20])#read first 20 chars but not including the 20th

#SEARCHING THROUGH A FILE
# fhand = open('mbox.txt')
# for line in fhand:
#     if line.startswith("From: "):
#         print(line)

#SEARCHING THROUGH A FILE(FIXED)
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("From: "):
#         print(line)

# SKIPPING WITH CONTINUE
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From: "):
#         continue
#     print(line)

#USING IN TO SELECT LINES
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@bensonmakau' in line:
#         continue
#     print(line)

#PROMPT FOR FILE NAME
# fname = input("Enter the file name: ")
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject'):
#         count = count + 1
    
#     print("There were", count, 'subject lines in', fname)

# EXCEPTION HANDLING
# fname = input("Enter the file name: ")
    
# try:
#   fhand = open(fname)
# except:
#   print("File cannot be opened!", fname)
#   quit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject'):
#         count = count + 1
#     print("There were", count, 'subject lines in', fname)

#LISTS
# mylist = [1,15,25,78,95]

#LOOPING THROUGH A LIST
# for i in mylist:
#     print(i)
# print("Blastoff")

#READ VALUES IN A LIST
# friends = ['Joseph','Glenn','Sally']
# print(friends[1])#output :Glenn
# #length of a list
# print(len(friends))
#strings in lists are not changeble

#RANGE FUNCTION RETURNS A LIST OF
# NUMBERS THAT RANGE FROM ZERO TO ONE LESS 
# THAN THE PARAMETER
# print(range(len(friends)))

#looping using range(len(friends))
# for friend in friends:
#     print("Happy New Year: ", friend)
# for i in range(len(friends)):
#     friend = friends[i]
#     print("Happy New Year: ", friend)


#CONCATINATING LISTS
# a= [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)
#SLICING LISTS
# t =[9,41,12,3,74,15]
# t[1:3]#output[41,12]
#LIST METHODS
#append, count,extend, index, insert,pop,remove,reverse,sort

#BUILDING A LIST FROM SCRATCH
# stuff = list()
# stuff.append('book')
# stuff.append('99')
# print(stuff)
# stuff.append('cookie')
# print(stuff)

#IS SOMETHING IN THE LIST
# some = [1,9,21,10,16]
# print(9 in some)
# print(2 not in some)print(9 in some)

#SORTING LISTS
friends = ['Joseph','Sally','Glenn']
friends.sort()
print(friends)

#FUNCTIONS TO MANIPULATE LISTS
nums = [3,41,12,9,74,15]
print(len(nums))#length of list
print(max(nums))#max value in the list
print(min(nums))#min value in the list
print(sum(nums))#sum value of the list elements
print(sum(nums)/len(nums))#average