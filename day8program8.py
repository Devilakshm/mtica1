def checkEven(num1):
    if num1%2==0:
        return "Even"
    return None
def checkOdd(num1):
    if num1%2==1:
        return "Odd"
    return None
num=(int(input("enter a number:")))
#print(checkEven(num))
#print(checkOdd(num))
x=checkEven(num)
y=checkOdd(num)
print("x=", x)
print("y=", y)
