# square the elements in the list
data = [1, 2, 3]
# solution
data_squared = [i*i for i in data]
data_squared = list(map(data, lambda x: x*x))

# sort below list
data = [(1,2), (2,3), (4,1)]
# solution
data_sorted = sorted(data, key=lambda x: x[1])

# create generator to square the elements from 0-10
# solution
def square_elements():
    for i in range(10):
        yield i*i

# find smallest common elements from below three list, don't use pythonic features
a = [1,2,3,4,5]
b = [2,3,7,8]
c = [3,9]

# solution
def smallest_common_min_element(list_1, list_2, list_3):
    # create pointers for each list
    i, j, k = 0, 0, 0

    a_len = len(a)
    b_len = len(b)
    c_len = len(c)

    min_item = None

    while i < a_len and j < b_len and k < c_len:
        if a[i] == b[j] == c[k]:
            min_item = a[i]
            break
        elif a[i]<b[j]:
            i += 1
        elif b[j]<c[k]:
            j += 1
        else:
            k += 1

    return min_item


a = [1, 2, 5, 6, 8, 9]
b = [3, 4, 5, 9, 10, 11, 16]
c = [3, 4, 6, 7, 8, 9]

print(smallest_common_min_element(a, b, c))

# how will you read file having one million urls
# design database tables showing many to many relationship between books and authors, one book can have many authors and an author can have many books




