# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root== None: return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.right !=None or root.left !=None or root.val==1:
            return root
        else: return None
        
