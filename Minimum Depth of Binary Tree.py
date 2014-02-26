# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def getMinDepth(self, root, depth):
        if root.left == None and root.right == None:
            return depth
        if root.left == None:
            return self.getMinDepth(root.right, depth+1)
        elif root.right == None:
            return self.getMinDepth(root.left, depth+1)
        else:
            return min(self.getMinDepth(root.left, depth+1), self.getMinDepth(root.right, depth+1))
    
    def minDepth(self, root):
        if root == None:
            return 0
        return self.getMinDepth(root, 1)
        
