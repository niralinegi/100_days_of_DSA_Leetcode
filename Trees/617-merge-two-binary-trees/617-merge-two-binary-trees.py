# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1, root2)
    
    def merge(self, t1, t2):
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        newNode = TreeNode(t1.val+t2.val)
        newNode.left = self.merge(t1.left, t2.left)
        newNode.right = self.merge(t1.right, t2.right)
        
        return newNode
        
