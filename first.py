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
astr = 'hello bob'
try:
    istr = int(astr)
except Exception as e:
    warning ="something went wrong"
    print(warning)


astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second', istr)
