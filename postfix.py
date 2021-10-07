from collections import deque


def postfixchecker(exp):

    stack = deque()

    for ch in exp:

        if ch.isdigit():
            stack.append(int(ch))

        else:
            x = stack.pop()
            y = stack.pop()

            if ch == 'x':
                stack.append(x*y)

            elif ch == '+':
                stack.append(x+y)
            elif ch == '-':
                stack.append(y-x)
            elif ch == '/':
                stack.append(y//x)

    return stack.pop()


exp = "138x+"
print(postfixchecker(exp))
