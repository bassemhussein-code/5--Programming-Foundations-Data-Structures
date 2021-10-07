class Stack():
    def __init__(self, n):
        self.arr = [None]*n
        self.capacity = n
        self.top1 = -1
        self.top2 = n

    def push1(self, key):

        if self.top1 + 1 == self.top2:
            print("Stack overflow")
            exit(-1)

        self.top1 = self.top1 + 1
        self.arr[self.top1] = key

    def push2(self, key):

        if self.top1 + 1 == self.top2:
            print('stack overflow')
            exit(-1)

        self.top2 = self.top2 - 1
        self.arr[self.top2] == key

    def pop1(self):
        if self.top1 < 0:
            print('stack underflow ')
            print('empty stack')
            exit(-1)

        top = self.arr[self.top1]

        self.top1 = self.top1 - 1
        return top

    def pop2(self):
        if self.top2 >= self.capacity:
            print('Stack over')
            print('there is no place to pop items from ')
            exit(-1)

        top = self.arr[self.top2]
        self.top2 = self.top2 + 1
        return top


first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]


stack = Stack((len(first) + len(second)))
[stack.push1(i) for i in first]

# [stack.push2(i)for i in second]

print(stack.pop1())
print(stack.pop1())
stack.push1(3)
print(stack.pop1())
[stack.push2(i) for i in second]
