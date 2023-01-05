class Complex:
    def __init__(self,real,imag):
          self.real=real
          self.imag=imag
    def __sub__(self,ob):
        temp=(self.real*ob.real-self.imag*ob.imag,
        self.real*ob.imag+self.imag*ob.real)
        
        return temp
    def __str__(self):
        return(self.real,self.imag)
ob1=Complex(1,3)
ob2=Complex(2,6)
#ob3=ob1.add(ob2)
ob3=ob1-ob2

print(ob3)
    
