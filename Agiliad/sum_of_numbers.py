# calculate sum of all the numbers, for example, num = 12345; sum=14

def sum_of_number(num):
    s = 0
    while num:
        s += num%10
        num = num//10

    return s


assert(sum_of_number(12345)) == 15
assert(sum_of_number(1234)) == 10
assert(sum_of_number(111)) == 3
assert(sum_of_number(000)) == 0
assert(sum_of_number(1111000112)) == 8