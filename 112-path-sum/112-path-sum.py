# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.pathSum(root, targetSum-root.val)
    
    def pathSum(self, root, targetSum):
        
        if root.left is None and root.right is None and targetSum == 0:
            return True
        
        if root.left is None and root.right is None and targetSum != 0:
            return False
        
        leftAns = False
        rightAns = False
        
        if root.left is not None:
            leftAns = self.pathSum(root.left, targetSum-root.left.val)
            
        if root.right is not None:
            rightAns = self.pathSum(root.right, targetSum-root.right.val)
            
        return leftAns or rightAns