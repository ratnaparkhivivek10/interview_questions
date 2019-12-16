# Using stack
def check_balanced_braces(braces):
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']

    brace_stack = []
    # empty string - return true
    if not braces:
        return True
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
                else:
                    break
    
    if brace_stack:
        return False
    else:
        return True


assert check_balanced_braces('') == True
assert check_balanced_braces('{') == False
assert check_balanced_braces('{})') == False
assert check_balanced_braces('{}[]()') == True
assert check_balanced_braces('{[}]') == False
assert check_balanced_braces('{[()]}') == True
assert check_balanced_braces('{[(])}') == False
assert check_balanced_braces('{{[[(())]]}}') == True
assert check_balanced_braces('}][}}(}][))]') == False
assert check_balanced_braces('[](){()}') == True
assert check_balanced_braces('()') == True
assert check_balanced_braces('({}([][]))[]()') == True
assert check_balanced_braces('{)[](}]}]}))}(())(') == False
assert check_balanced_braces('([[)') == False
assert check_balanced_braces('({]])]})]}([)}{][)]{}{(])}([]}])})}([]}({}([{][{}') == False
