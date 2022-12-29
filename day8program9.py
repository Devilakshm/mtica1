def checkEvenOdd(num1):
    assert(num1>0),"Negative numbers"
    if num%2==0:
        return "Even"
    else:
        return "Odd"

for i in range(4):
    num=int(input("enter a  number:"))
    try:
        print(num,"is",checkEvenOdd(num))
    except AssertionError as ob:
            print(ob)
            
