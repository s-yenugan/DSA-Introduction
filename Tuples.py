 #Tuples are inmutable 
myTup = (2, 3, 4, 5, True, "Hello")
print(myTup, type(myTup))

#to access element
myTup = (2, 3, 4, 5, True, "Hello")
for value in myTup:
    print(value)
print(myTup[1:4])
print(myTup[4])

#covert tumple to list to make it mutable
myTup = (2, 3, 4, 5, True, "Hello")
new = list(myTup)
new[1] = 4 
print(new)

#unpacking in tuples
myTup = (1, 2, 3, 4, 5)
(first ,second, *third) = myTup
print(first, second, third)