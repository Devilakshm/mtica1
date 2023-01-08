import sys
print("coming throught stdout")
save_stdout =sys.stdout
fh=open(r"D:\pythonpractice10\Day17\lakshmi.txt","w")
sys.stdout =fh
print("this line goes to lakshmi.txt")
print(input())
sys.stdout=save_stdout
fh.close()
