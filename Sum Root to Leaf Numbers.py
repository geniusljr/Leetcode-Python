# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def getSum(self, root, curSum, total):
        if root == None:
            return;
        curSum = curSum * 10 + root.val;
        if root.left == None and root.right == None:
            total[0] += curSum
            return
        self.getSum(root.left, curSum, total)
        self.getSum(root.right, curSum, total)

    def sumNumbers(self, root):
        total = [0]
        self.getSum(root, 0, total)
        return total[0]
            
