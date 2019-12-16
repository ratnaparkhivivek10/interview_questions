'''
Given unsorted list of numbers print sum of all the elements excluding min and max
Input: [1, 3, 2, 4]
Output: 9, 6
9 = (10 - 1)
6 = (10 - 4)
'''

def min_max_sum(data):
    mn = data[0]
    mx = data[0]
    
    total = 0
    
    for num in data:
        total += num
        
        if num < mn:
            mn = num
        if num > mx:
            mx = num

    return [total - mn, total - mx]


assert min_max_sum([3, 1, 4, 2]) == [9, 6]
assert min_max_sum([3, 1, 4, 2, 5]) == [14, 10]
assert min_max_sum([1, 2, 3, 4]) == [9, 6]


