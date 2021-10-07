class Node():
    def __init__(self, key, next=None):

        self.key = key
        self.next = next


class Stack():
    def __init__(self):
        self.top = None

    def push(self, x):

        # allocate a new node in a heap

        node = Node(x)

        if node is None:
            print("heap overflow")

        print('inserting ', x)

        node.data = x

        node.next = self.top

        self.top = node

    def isEmpty(self):
        return self.top is None

    def peek(self):

        if not self.isEmpty():

            return self.top.data

        else:
            print('the stack is empty')
            return -1

    def pop(self):

        if self.top is None:
            print('the underflow')

        print('removing', self.peek())

        self.top = self.top.next
