#1: what will be the output of following programs

def decorator(func):
    def wrapper():
        print('wrapper called')
    return wrapper


@decorator
def f():
    print('f called')

#f = decorator(f)

del decorator

f()
#>> wrapper called

#2: what is output of following code, how will you fix it without modifying code?
str = 5
# convert this number into string.
str_num = str(5) # this won't work since str is not pointed to 5 due to bad naming practice.

import builtins
str_num = builtins.str(5)

# what is output of the following
class Person(object):
    cls_attr = 5
    def __init__(self, name):
        self.name = name
        self.cls_attr = 7


jane = Person('Jane')

jane.cls_attr
#>> 7
del jane.cls_attr # this has deleted instance attribute
jane.cls_attr
#>> 5

del jane.cls_attr
# >> this will not delete class attribute. Throws attribute error exception as it does not find "cls_attr" in jane.__dict__

#3: what will be output of following program?
class Person(object):
    def __init__(self, name):
        self.name = name
        return 0

#>> this will fail as init method should not return anything apart from None. It will still work if you explicitely return None like below.

class Person(object):
    def __init__(self, name):
        self.name = name
        return None
# This will still work.
