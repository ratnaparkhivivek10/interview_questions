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
            self.left = BinaryTree(data)
        else:
            self.right = BinaryTree(data)
        
