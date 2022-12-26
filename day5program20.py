def count_digit(s):
    n_digit=0
    for i in s:
        #print("i=",i)
        if i in '80123467648':
            n_digit+=1
            #print("i:",i,"temp_digit:",temp_digit)
    return n_digit
str1=input()
a=count_digit(str1)
print("no of digit in:' ",str1," 'is",a)
      
