'''
Implement binary search tree.
'''
class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.append(data)
        else:
            if self.right is None:
                self.right = BinaryTree(data)
            else:
                self.right.append(data)
        
