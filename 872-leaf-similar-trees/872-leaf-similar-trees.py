# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafsOfT1 = []
        leafsOfT2 = []
        
        self.findLeaves(root1, leafsOfT1)
        self.findLeaves(root2, leafsOfT2)
        
        return (leafsOfT1 == leafsOfT2)
    
    def findLeaves(self, root, leaves):
        
        if root is None:
            return
        
        if root.left is None and root.right is None:
            leaves.append(root.val)
            
        self.findLeaves(root.left, leaves)
        self.findLeaves(root.right, leaves)
            
        return