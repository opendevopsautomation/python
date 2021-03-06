#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        """
        :type root: TreeNode
        :rtype: List[float]
        """        
        result = []
        queue = [root]
        while queue:
            total, cnt = 0, len(queue)
            for _ in range(cnt):
                node = queue.pop(0)
                total += node.val 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(total/cnt)
        return result