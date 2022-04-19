# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.preorder(root, answer)
        return answer
    
    def preorder(self, root, answer):
        if root is None:
            return
        
        answer.append(root.val)
        self.preorder(root.left, answer)
        self.preorder(root.right, answer)
        