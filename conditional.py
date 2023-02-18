number = 5
if number > 2 and number != 0:
    print('Number is bigger than 2')
elif number < 2:
    print('Number is smaller than 2')
else:
    print('Wrong number')


class Foo(object):
    def __init__(self, item) -> None:
        self.my_item = item
    def __eq__(self, other) -> bool:
        return self.my_item == other.my_item

a = Foo(5)
b = Foo(5)

print(a == b) # true