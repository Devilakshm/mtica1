def printMonthName(dn):
    if (dn==1):
         return "january"
    if(dn==2):
         return "february"
    elif(dn==3):
        return "march"
    elif(dn==4):
        return "April"
    elif(dn==5):
        return "may"
    elif(dn==6):
        return "june"
    elif(dn==7):
        return "July"
    elif(dn==8):
        return "August"
    elif(dn==9):
        return "September"
    elif(dn==10):
        return "october"
    elif(dn==11):
        return "November"
    elif(dn==12):
        return "december"
    else:
     return "Invalid"
    
    
    pass
for i in range(13):
    inpNum=int(input())
    print(printMonthName(inpNum))
