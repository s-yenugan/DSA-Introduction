n = int(input("Enter a Number: " ))
m = int(input("Enter a Number: "))
for currRow in range(n):
    for currCol in range(m):
        print (currCol+1, end= "")
    print("")
    
n = int(input("Enter a Number"))
for currRow in range(n):
    for currCol in range(n):
        if currCol <= currRow:
           print(currCol+1, end = "")
        else:
            print(" ", end= " ")
    print("")
    
n = int(input())
for currRow in range(n):
    for currCol in range (n):
        if (currCol < n-(currRow+1)):
            print(" ", end= " ")
        else: 
            print ("*", end=" ")
    print("")
        
