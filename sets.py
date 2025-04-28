#set is used to store values but without indexing and doesnt support duplicate values
'''mySet = {2 , 3 , 4, 5, True, "adobe"}
for value in mySet:
    print(mySet)
print(mySet, type(mySet))'''

#methods in string add, update, remove, pop, clear
mySet = {2 , 3 , 4, 5, True, "adobe"}
mySet2 = {6, 7, 9}
mySet.update(mySet2)
mySet.remove(5)
mySet.pop()
mySet.clear()
mySet.add ("google")
print(mySet)
