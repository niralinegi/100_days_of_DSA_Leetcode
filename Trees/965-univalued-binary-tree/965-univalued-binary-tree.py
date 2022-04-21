# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.check_uni(root, root.val)
    
    def check_uni(self, root, ans):
        if root is None:
            return True
        
        if root.val != ans:
            return False
        
        return self.check_uni(root.left, ans) and self.check_uni(root.right, ans)
        
        
