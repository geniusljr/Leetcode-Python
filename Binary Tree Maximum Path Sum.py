# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    
    def maxPathSum(self, root):
        maxSum = [-10000]
        
        def maxBranchSum(root, maxSum):
            leftBranchSum = -10000 if root.left == None else maxBranchSum(root.left, maxSum)
            rightBranchSum = -10000 if root.right == None else maxBranchSum(root.right, maxSum)
            temp = root.val + max([leftBranchSum, 0]) + max([rightBranchSum, 0])
            maxSum[0] = max(maxSum[0], temp)
            maxBranch = max([leftBranchSum, rightBranchSum])
            return root.val + max([maxBranch, 0])
        
        maxBranchSum(root, maxSum)
        return maxSum[0]
    
    