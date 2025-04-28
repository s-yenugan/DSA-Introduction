#hashmap
'''myDict = {"student1" : 49, "student2": 50}
print(myDict.get("student1"))'''

#To add new value keys.values,items
myDict = {"student1" : 49, "student2": 50, "student3" : 87}
for key, value in myDict.items():
    print(key,value)

#To check if the key is present in dict
myDict = {"student1" : 49, "student2": 50, "student3" : 87}
targetKey = "student1"
if targetKey in myDict:
    print("present")
    

    