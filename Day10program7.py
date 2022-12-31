fo1=open(r"C:\pythonpractice(29)\Day10\abcde.txt","r")
fo2=open(r"C:\pythonpractice(29)\Day10\lakshmiA.txt","w+")
temp=fo1.read()
fo2.write(temp)
fo1.close()
fo2.close()
print("file copied")

