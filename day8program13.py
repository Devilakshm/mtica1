def addNumber(num1,num2):
    res=num1+num2
    return res
for i in range(6):
    inp1=int(input("enter a number:"))
    inp2=int(input("enter a number:"))
    print(inp1,'+',inp2,'=',addNumber(inp1,inp2),sep='')
