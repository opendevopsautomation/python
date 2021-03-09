# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root        
        queue=[root]
        level=1
        while level !=d-1:
            cnt=len(queue)
            level+=1
            for _ in range(cnt):
                node=queue.pop(0)                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        for _ in range(len(queue)):
            current_node = queue.pop(0)

            left = current_node.left
            right = current_node.right

            new_node1 = TreeNode(v)
            new_node2 = TreeNode(v)

            current_node.left = new_node1
            new_node1.left = left

            current_node.right = new_node2
            new_node2.right = right                    
        return   root    

                    
                    
                    
