test_string = 'Arora'

rev = test_string[::-1]
print(rev)
if rev.lower() == test_string.lower():
    print("yes")
else:
    print("no")

#string[a:b:c] is a slicing notation that is used to describe how to slice through a string.
#the 'c' indicates the increment integer value, a is the integer start value and b is integer end value
print(reversed(test_string.lower()))
if test_string.lower()==reversed(test_string.lower()):
    print("yes")
else:
    print("no")