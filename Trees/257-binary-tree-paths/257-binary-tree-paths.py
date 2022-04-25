# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        self.rootToLeafPath(root, ''+str(root.val), answer)
        return answer
    
    def rootToLeafPath(self, root, currentPath, answer):
        
        if root.left == None and root.right == None:
            answer.append(currentPath)
            return
        
        if root.left != None:
            self.rootToLeafPath(root.left, currentPath+'->'+str(root.left.val), answer)
            
        if root.right != None:
            self.rootToLeafPath(root.right, currentPath+'->'+str(root.right.val), answer)
            
        return
        
