"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        self.preorder_traversal(root, answer)
        return answer
        
    def preorder_traversal(self, root, answer):
        if root is None:
            return
        
        answer.append(root.val)
        
        for curr_child in root.children:
            self.preorder_traversal(curr_child, answer)
            
        return