class Stack():

    def __init__(self, size):
        self.arr = [None]*size
        self.capacity = size
        self.top = -1

    def push(self, x):
        if self.isFull():
            print("Stack is full !! ")
            exit(1)

        print('inserting ', x, "into the stack")
        self.top = self.top + 1
        self.arr[self.top] = x

    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.arr[self.top]

    def pop(self):
        if self.isEmpty():
            print('the stack is empty .. no place to pop item')

            exit(1)

        print('Removing ', self.peek(), "from the stack")

        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def isFull(self):
        return self.size() == self.capacity

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.top + 1


stack = Stack(3)
stack.push(1)
print('*'*20)
print(stack.isEmpty())
print('*'*20)
stack.pop()
print('*'*20)
print(stack.isFull())
print('*'*20)
print(stack.isEmpty())
print('*'*20)
stack.push(77)
print('*'*20)
stack.push(00)
print('*'*20)
print(stack.peek())
print(stack.peek())
stack.push(5)
print('*'*20)
print(stack.peek())
print('*'*20)
print(stack.isFull())
print('*'*20)
stack.pop()
print(stack.peek())
stack.pop()
print('*'*20)
print(stack.peek())
print(stack.isEmpty())
print('*'*20)
stack.pop()
print('*'*20)
print(stack.isEmpty())
