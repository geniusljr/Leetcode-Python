# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        inorderArr = self.inorder(root)
        first, second = -1, -1
        for i in range(0, len(inorderArr)-1):
            if inorderArr[i].val > inorderArr[i+1].val:
                first = i if first == -1 else first
                second = i+1
        if first != -1 and second != -1:
            inorderArr[first].val ^= inorderArr[second].val
            inorderArr[second].val ^= inorderArr[first].val
            inorderArr[first].val ^= inorderArr[second].val
        return root
        
    def inorder(self, root):
        results = []
        if root == None:
            return results
        results = self.inorder(root.left) + [root] + self.inorder(root.right)
        return results
        
