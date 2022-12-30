def printDay(dn):
    if (dn==0):
        da= "Sunday"
    elif(dn==1):
        da= "Monday"
    elif(dn==2):
        da= "Tuesday"
    elif(dn==3):
        da= "wednesday"
    elif(dn==4):
        da= "Thrusday"
    elif(dn==5):
        da= "friday"
    elif(dn==6):
        da="Satuarday"
    return da
def printDay1(dn):
    if (dn==0):
         da= "Sunday"
    if(dn==1):
         da= "Monday"
    if(dn==2):
        da= "Tuesday"
    if(dn==3):
        da= "wednesday"
    if(dn==4):
        da= "Thrusday"
    if(dn==5):
       da= "friday"
    if(dn==6):
       da="Satuarday"
    return da
##for i in range(7):
##    inpNum=int(input())
##    print(printDay(inpNum))
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print(time.time()-start)
    start=time.time()
    print(printDay(inpNum))
    print(time.time()-start)
    
