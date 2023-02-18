from enum import Enum

class Color(Enum):
    red = 1
    orange = 2
    blue = 3

print(Color.red)
print(Color(1))