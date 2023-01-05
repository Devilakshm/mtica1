class A:
    def first_method(self):
        print("method of class A..")
B().first_method()
class B(A):
    def second_method(self):
        print("method of class B...")
        super().first_method()
ob=B()
ob.first_method()
