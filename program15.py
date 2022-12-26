def count_vowel(s):
    temp_vowel=0
    for i in s:
       # print("i=",i)
        if i in 'AEIOUaeiou':
            temp_vowel+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return temp_vowel
str1=input()
a=count_vowel(str1)
print("on of vowel in:'",str1,"'is",a)
