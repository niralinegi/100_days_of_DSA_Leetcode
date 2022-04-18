"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.height(root)
    
    def height(self, root):
        if root is None:
            return 0
        
        ans = 0
        
        for currNode in root.children:
            ans = max(ans, self.height(currNode))
            
        return 1+ans
        