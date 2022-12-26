def extract_specialcharacter(s):
    temp_specialcharacter=''
    for i not in s:
        print("i=",i)
        if i in 'lakshmi@likhi%$#':
            temp_specialcharacter+=i
            print("i:",i,"temp_specialcharacter:",temp_specialcharacter)
    return temp_specialcharacter
str1=input()
a=extract_specialcharacter(str1)
print("on of specialcharacter :",a)

