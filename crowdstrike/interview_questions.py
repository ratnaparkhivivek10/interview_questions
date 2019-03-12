#Q1 - square the elements in the list
data = [1, 2, 3]
# solution
data_squared = [i*i for i in data]
data_squared = list(map(lambda x: x*x, data))

#Q2 - sort below list
data = [(1,2), (2,3), (4,1)]
# solution
data_sorted = sorted(data, key=lambda x: x[1])

#Q3 - create generator to square the elements from 0-10
# solution
def square_elements():
    for i in range(10):
        yield i*i

#Q4 - find smallest common elements from below three list, don't use pythonic features
a = [1,2,3,4,5]
b = [2,3,7,8]
c = [3,9]

#Q5 - solution - return smallest single element
def smallest_common_min_element(list_1, list_2, list_3):
    # create pointers for each list
    i, j, k = 0, 0, 0

    a_len = len(list_1)
    b_len = len(list_2)
    c_len = len(list_3)

    min_item = None

    while i < a_len and j < b_len and k < c_len:
        if list_1[i] == list_2[j] == list_3[k]:
            min_item = list_1[i]
            break
        elif list_1[i] < list_2[j]:
            i += 1
        elif list_2[j] < list_3[k]:
            j += 1
        else:
            k += 1

    return min_item

# solution - return all common elements
def common_elements(list_1, list_2, list_3):
    i, j, k = 0, 0, 0
    
    l1_len = len(list_1)
    l2_len = len(list_2)
    l3_len = len(list_3)

    while i < l1_len and j < l2_len and k < l3_len:
        if list_1[i] == list_2[j] == list_3[k]:
            # can print any one of the list element
            print(list_1[i])
            i += 1
            j += 1
            k += 1
        elif list_1[i] < list_2[j]:
            i += 1
        elif list_2[j] < list_3[k]:
            j += 1
        else:
            k += 1


# test data
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [3, 4, 5, 7, 9, 10, 11, 16]
c = [3, 4, 6, 7, 8, 9]

# try first solution
print(smallest_common_min_element(a, b, c))

# try second solution
common_elements(a, b, c)

#Q6 - how will you read file having one million urls
#Q7 - design database tables showing many to many relationship between books and authors, one book can have many authors and an author can have many books