from collections import deque


def reverse(str):

    stack = deque(str)

    return " ".join(stack.pop()for _ in range(len(str)))


str = "Reverse Me"
str = reverse(str)

print(str)
