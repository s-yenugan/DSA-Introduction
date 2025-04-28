#Loop is a statement executed repeatedly. There are two types of loops for loop and while loop
#Syntax of for loop
'''for iterator in seq:
    statements'''
for i in range(5):
    print(i)

n = int(input())
sum = 0
for i in range (n):
    sum += i+1
print(sum)
    
# range accepts 3 arguments from which point to start, end point(n-1), step argument
for i in range (3, 10, 3):
    print(i)
    
#...... take n as input and provide output of 0*0*0*.......n
n = int(input())
for i in range (n):
    if i%2 == 0:
        print("0", end = '')
    else:
        print("*", end = '')
print('')

#Syntax of while loop
'''while condition :
    statements
    icrement/decrement'''
    
n = int(input())
i = 0
while i <= n:
    if i % 2 == 0:
    
        print("0", end= '')
    else:
        print("*", end= '')
    i += 1
print("")