#Slicing and List comprehension
'''myList = [10,20,30,40,50]
print(myList[0:3])

myList = [int(ele) for ele in input().split()]
print(myList)

#2D List
grid = [[2,3,4],[5,6,4],[8,9,6]]
print(grid[0][2])

#To take input
n = int(input())
m = int(input())
grid =[]
for i in range (n):
    temp = input().split()
    for j in range (m):
        temp[j] = int(temp[j])
    grid.append(temp)
print(grid)

#taking input using list comprehension
n = int(input())
m = int(input())
grid = []
for i in range (n):
   grid.append([int(ele) for ele in input().split()])
print(grid)

# Problem to take trace of a matrix 
n = int(input())
matrix=[]
for i in range (n):
    matrix.append([int(ele) for ele in input().split()])
trace = []
for i in range (n):
    trace.append(matrix[i][i])
print(trace)'''

#Transpose of a matrix
n = int(input())
matrix = []
for i in range (n):
    matrix.append([int(item) for item in input().split()])
for i in range (n):
    for j in range (n):
        if j > i:
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
            
for i in range(n):
    print(matrix[i])
    
    
    
    