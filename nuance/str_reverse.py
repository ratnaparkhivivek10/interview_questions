'''
Reverse the string except special characters
Input: 'abc#$pqr'
Output: 'cba#$rqp'
'''


def str_reverse(s):
    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    prefix = ''
    suffix = ''
    flag = 0
    
    for c in s:
        if c in special_chars:
            prefix = prefix + c
            flag = 1
        else:
            if flag:
                suffix = c + suffix
            else:
                prefix = c + prefix

    return prefix + suffix


assert str_reverse('abc#$pqr') == 'cba#$rqp'
assert str_reverse('abcd#$%pqr') == 'dcba#$%rqp'
assert str_reverse('c#$p') == 'c#$p'



def str_reverse2(s):
    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    head = ''
    tail = ''
    
    i = 0
    j = len(s)-1

    while True:
        if s[i] not in special_chars:
            head = s[i] + head
            i += 1
        if s[j] not in special_chars:
            tail = tail + s[j]
            j -= 1

        if s[i] in special_chars and s[j] in special_chars:
            break

    return head+s[i:j+1]+tail


assert str_reverse2('abc#$pqr') == 'cba#$rqp'
assert str_reverse2('abcd#$%pqr') == 'dcba#$%rqp'
assert str_reverse2('c#$p') == 'c#$p'
