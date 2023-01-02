##def printpattern(ch,n):
##    for i in range(n+1):
##     print(ch*i)
##ch=input()
##
##n=int(input())   
##printpattern(ch,n)


def printpattern(s,n):
    assert(n>=0),'INVALID'
    for i in range(n,0,-1):
        print(s*i)
s=input()
n=int(input())
try:
    printpattern(s,n)
except AssertionError as a:
    print(a)
    
        

