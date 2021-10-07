from collections import deque


def balParenthesis(exp):

    if len(exp) & 1:
        return False

    stack = deque()

    for ch in exp:

        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')

        elif ch == '[':
            stack.append(']')

            # the pop operation will occur
            # the pop operation will occur
            #  the pop operation will occur

        elif not stack or stack.pop() != ch:
            return False

    return not stack


exp = "{()}[{}}]"

if balParenthesis(exp):
    print('balanced expersion')


else:
    print('unbalanced expersion')
