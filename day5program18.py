def count_specialcharacter(s):
    n_specialcharacter=0
    for i  in s:
        #print("i=",i)
        if i not in 'lakshmi@likitha$@':
            n_specialcharacter+=1
            #print("i:",i,"temp_specialcharacter:",temp_specialcharacter)
    return n_specialcharacter
str1=input()
a=count_specialcharacter(str1)
print("on of specialcharacter :",a)
