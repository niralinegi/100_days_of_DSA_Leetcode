# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftLeafSum(root, False)
        
    def leftLeafSum(self, root, onLeftLeaf):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            if onLeftLeaf:
                return root.val
            else:
                return 0
            
        leftAns = self.leftLeafSum(root.left, True)
        rightAns = self.leftLeafSum(root.right, False)
        
        return leftAns + rightAns
