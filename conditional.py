#Conditional Statements 
'''We have three conditional statements (if, elif, else)'''

#Using if statement 
a = int(input())

#Syntax of if statement
#if condition:
#   statements

if a%2 == 0:
    print("It is Divisible")
print('It is not Divisible')

# Using else statement
n = int(input("Enter a number: "))

#Syntax of if statement
#if condition:
#   statements
#else:
#    statemets

if n%2 == 0:
    print("Divisible")
else:
    print("Not Divisible")

# Using elif statement
b = int(input("Enter a Number: "))
if b%2 == 0:
    print("It is Even")
elif b%3 == 0:
    print("It is not even divisible by 3")
else:
    print("It is Odd")

    

