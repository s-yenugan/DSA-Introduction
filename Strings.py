#Methods in string
#count returns number of elements occured in a string
'''myStr = input()
print(myStr.count('o'))

#split method
myStr = input()
print(myStr.split('o'))

#strip method
myStr = " banana "
print(myStr.strip())

#Askii values A = 65 B = 66 .... Z = 90 a = 97.... z =122

x = 'b'
print (x, ord(x),chr(ord(x) + 3))

#problem 

myStr = "AAjhFa"
ans =""
for i in range(len(myStr)):
    if ord(myStr[i])>90:
        ans += myStr[i]
    else:
        ans += chr(ord(myStr[i])+ ord('a')-ord('A'))
print(ans)'''

#check if string is palandrome or not

myStr = input()
ispalindrome = True
for i in range (len(myStr)//2):
    if myStr[i] != myStr[len(myStr) - i - 1]:
        ispalindrome = False
if ispalindrome:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
 