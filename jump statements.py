#Jump statements in python (continue, break)

#continue is to used to skip iteration

n = 4
for i in range(1, n+1):
    temp = i
    while temp%2 == 0:
        temp /= 2
    if temp == 1:
        continue
        
    print(i)
    
#break is to stop the iteration

n = 4
for i in range (1, n-1):
    temp = i
    while temp%2 == 0:
        temp /= 2
    if temp != 1:
        break
    print(i)
