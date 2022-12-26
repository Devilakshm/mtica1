def count_vowel(s):
    temp_digits=''
    for i in s:
        print("i=",i)
        if i in 'AEIOUaeiou':
            temp_vowel+=i
            print("i:",i,"temp_vowel:",temp_vowel)
    return temp_vowel
str1=input()
a=extract_vowel(str1)
print("on of vowel :",a)
