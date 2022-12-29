##num1=input("Enter a number:")
##num2=input("Enter a number:")
##try:
##    res=int(num1)/int(num2) #Excute with num2=non zero and zero
##except ZeroDivisionError:
##    print("Exception handle by Lakshmi")
##except ValueError:
##    print("Exception handle by Likhitha")
##except Exception as ob:
##    print(ob)
##else:
##    print(num1, '/' ,num2, '=', res)
##finally:
##     print("thanks")
##print("visit again at python class at MTICA")

num1=input("Enter a number:")
num2=input("Enter a number:")
try:
    res=int(num1)/int(num2) #Excute with num2=non zero and zero
except (ZeroDivisionError,ValueError):
    print("Exception handle by Lakshmi")

except Exception as ob:
   print(ob)
else:
   print(num1, '/' ,num2, '=', res)
finally:
     print("thanks")
print("visit again at python class at MTICA")



