# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parents = [0, 0]
        levels = [0, 0]
        
        self.findParentsAndLevel(root, TreeNode(-1), 0, x, y, parents, levels)
        
        return (parents[0] != parents[1]) and (levels[0] == levels[1])
    
    def findParentsAndLevel(self, root, currentParent, currentLevel, x, y, parents, levels):
        if root is None:
            return
        
        if root.val == x:
            parents[0] = currentParent.val
            levels[0] = currentLevel
            
        if root.val == y:
            parents[1] = currentParent.val
            levels[1] = currentLevel
            
        self.findParentsAndLevel(root.left, root, currentLevel+1, x, y, parents, levels)
        self.findParentsAndLevel(root.right, root, currentLevel+1, x, y, parents, levels)
        
        return