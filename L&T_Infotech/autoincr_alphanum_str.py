import itertools
import string

def alpha_num_auto_increment(str_width: int, num_width: int) -> str:
    '''
    str_width: number of letters in prefix, e.g. AAA or AA or AAAAAA or whatever.
    num_width: number of digits, e.g. 3, 4
    '''
    for prefix in itertools.product(string.ascii_uppercase, repeat=str_width):
        p = ''.join(prefix)
        for num in range(10**num_width):
            s = f'{num:0>{num_width}d}'

            yield p+s


for i in alpha_num_auto_increment(3, 2):
    print(i)
