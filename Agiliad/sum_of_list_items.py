# calculate sum of items in below list
# mylist = [1, [2, [3, [4, [5]]]]]

def sum_(mylist):
    if len(mylist) == 1:
        return mylist[0]
    s = mylist[0] + sum_(mylist[1])

    return s


lst = [1, [2, [3, [4, [5]]]]]
assert sum_(lst) == 15