class Node():
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.right = right
        self.left = left


def isIdentical(x, y):
    if x is None and y is None:
        return True

    return (x and y) and (x.key and y.key) and isIdentical(x.left, y.left) and isIdentical(x.right, x.right)


x = Node(15)
x.rigth = Node(40)
x.left = Node(30)

x.rigth.rigth = Node(60)

x.rigth.left = Node(50)

x.left.left = Node(30)
x.left.right = Node(20)


y = Node(15)

y.rigth = Node(40)
y.left = Node(30)
y.rigth.right = Node(60)
y.rigth.left = Node(50)

y.left.left = Node(30)
y.left.right = Node(20)


if isIdentical(x, y):
    print(' are two identical tree')


else:
    print('the two trees are not identical')
