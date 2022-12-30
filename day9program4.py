def printSeries(ch,n):
    sp=' .'
    for i in range(0,n):
        print(sp*(n-1)+ch*(i*2+1)+sp*(n-i-1))
    return None
inpch=input()
inpNum=int(input())
printSeries(inpch,inpNum)
