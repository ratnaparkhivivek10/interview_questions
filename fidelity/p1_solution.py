# Using stack
def check_balanced_braces(braces):
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']

    brace_stack = []

    # first closing bracket case - return false
    if braces[0] in closing:
        return False

    for brace in braces:
        if not brace_stack:
            brace_stack.append(brace)
        else:
            if brace in opening:
                brace_stack.append(brace)
            else:
                if opening.index(brace_stack[-1]) == closing.index(brace):
                    brace_stack.pop()
    
    if brace_stack:
        return False
    else:
        return True


data = '{}[]()'
data = '{[}]'
data = '{[()]}'
data = '}][}}(}][))]'
is_balanced = check_balanced_braces(data)

print(is_balanced)



import unittest

class BalancedBraceTest(unittest.TestCase):
    def test_balanced_braces(self):
        pass
