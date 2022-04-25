# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        self.rootToLeaf(root, ''+str(root.val), answer)
        return answer[0]
    
    def rootToLeaf(self, root, currentPath, answer):
        
        if root.left == None and root.right == None:
            answer[0] += int(currentPath, 2)
            return
        
        if root.left != None:
            self.rootToLeaf(root.left, currentPath+str(root.left.val), answer)
            
        if root.right != None:
            self.rootToLeaf(root.right, currentPath+str(root.right.val), answer)
            
        return
