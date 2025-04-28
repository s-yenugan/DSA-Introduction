myList = [10,20,30]
print(myList[0])
print(len(myList))

#List in build methods 

#To add an element we use append
myList = [20, 50, 30]
myList.append(40)
print(myList)

# Insert Method 

myList = [20, 50, 30]
myList.insert(1, 50)
print(myList)

#Pop Method (removes last element from the list)
myList = [20, 50, 30]
myList.pop()
print(myList)

# To take input of list
myList = []
n = int(input())
for i in range (n):
    newEle = int(input())
    myList.append(newEle)
print(myList)

# To take input using split
myList = input().split(" ")
for i in range(len(myList)):
    myList[i] = int(myList[i])
print(myList, type(myList))

#Problems on list 
#sum of list
n = int(input())
myList = input().split()
sumList = 0
for i in range (n):
    sumList += int(myList[i])
print(sumList)

#using sum function

n = int(input())
myList = input().split()
for i in range(n):
    myList[i] = int(myList[i])
print(sum(myList))

#To find min and max
n = int(input())
myList = input().split()
for i in range (n):
    myList[i] = int(myList[i])
minEle = myList[0]
maxEle = myList[0]
for val in myList:
    if val < minEle:
        
        minEle = val
    if val > maxEle:
        maxEle = val
print (minEle, maxEle)

#Using min,max function

n = int(input())
myList = input().split()
for i in range (n):
    myList[i]=int(myList[i])
minEle = min(myList)
maxEle = max(myList)
print(minEle, maxEle)

#mean, median, mode
#mean = sum of every elements / length
n = int(input())
myList = input().split()
sumOfList = 0
for val in myList:
    sumOfList += int(val)
print (sumOfList/len(myList))

#median = middle most element in a sorted array if its odd else it would be average of middle most elements in case of even

n = int(input())
myList = input().split()

for i in range (n):
    myList[i] = int(myList[i])
myList.sort()

if n%2== 1:
    print (myList[n//2])
else:
    a = myList[n//2 - 1]
    b = myList[n//2]
    print  ((a+b)/2)
    
#mode = element with highest frequency i.e that occurs most number of times

n = int(input)
myList = input().split()
for i in range (n):
    myList[i] = int(myList[i])
maxCount = 0
manEle = myList[0]
for currEle in myList:
    currCount = 0
    for eachEle in myList:
        if eachEle == currEle:
            currCount += 1
    if currCount > maxCount:
        maxCount = currCount
        manEle = currEle
print(manEle, maxCount)
    

    
    