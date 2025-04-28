def myFun1():
    print ("Function 1")
    myFun2()
def myFun2():
    print ("Function 2")
myFun1()
myFun2()

def myFun1(x):
    print(x)
    myFun1(x)
myFun1(3)

    