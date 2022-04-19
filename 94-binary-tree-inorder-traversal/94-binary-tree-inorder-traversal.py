# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.inorder(root, answer)
        return answer
    
    def inorder(self, root, answer):
        if root is None:
            return
        
        self.inorder(root.left, answer)
        answer.append(root.val)
        self.inorder(root.right, answer)
        
        return
        
        