#  Non Local Variable
def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

c = counter()
print(c())
print(c())
print(c())

# Global variables
x = 'Hello'

def change_local_x():
    x = 'Hi'
    print(x)

change_local_x() # Hi
print(x) # Hello

# Local varible

def foo():
    a = 5
    print(a)
    return a

# print(a) -> error
print(foo())