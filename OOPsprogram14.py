message='global scope'
def outer():
    def inner():
        print(message)
    inner()
outer()

def outer():
    message='outer scope'
    print(message)
    def inner():
        print('inner:',message)
    inner()
    print('outer:',message)
outer()

