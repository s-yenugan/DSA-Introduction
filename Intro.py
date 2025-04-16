#Reference in python
my_var = 15
print(my_var, id(my_var)) #variable gets assigned to a memory in the system and it gets assessed when called.In python theres a feature where two differnet variables with same values gets a same memory loaction 

my_var2 = 15
print(my_var, id(my_var))

#Arithmetic Operatiors
a = 23
b = 5
print(a+b) # Addition operator
print(a-b) #Subtraction operator
print(a*b) #Multiplication operator
print(a/b) #Division operator
print(a%b) #Modulus operator provides with reminder 
print(a**b) #Exponentiation operator, calculating the power of a number
print(a//b) #Floor division operator, which performs division and returns the integer part of the result, discarding any fractional part. 

''' For assigning we use assigning operators like +=, -=, **=, //= '''

''' For comparing two values we use comparative operations, generally used for conditional statements
==(equal to), >(greater than), <(less than), >=(greater than or equals to), <=(less than or equals to),!(not), != (Not Equals to)'''

print(3==4) # Returns False
print(4==4) # Returns True
print (4 != 4) # != Reverses the given condition if the given statement is true it returns false, if it is false it returns true.

'''Locical operators are of three types and or not these are three main used operators. Using these we can combine two conditions written by comparatives'''

print (3==3 and 4==4) # Returns true only if both the conditons satisfy, incase if any of the condition fails it resturns false
print (3==2 or 4==4) # Returns true if any one of the given condition gets satisfied, incase of both the conditons dont satisfy it returns false.
print (not 3==3) # Inverses the condition if its true returns false if false returns true.