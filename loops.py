# while

i = 0
while i < 7:
    print(i)
    if i == 4:
        print('Break')
        break
    i += 1

# 0
# 1
# 2
# 3
# 4
# Break

# For Loop
number = [1,2,3,4,5,6]
numbers = (1,2,3,4,5,5,'a')

def looping(arr: list):
    for i in arr:
        if i % 2 == 0 :
            print(i)

looping(number)
print(type(number))
print(type(numbers))

# Iterating dics
d = {'a': 1, 'b': 2}

for k in d:
    print(k) #keys

for v in d.values():
    print(v) #values

