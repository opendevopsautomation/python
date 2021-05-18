# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        def bst(list):
            mid=len(list)//2
            if not list:
                return
            else:
                temp=TreeNode()
                node=temp
                node.val=list[mid]
                node.left=bst(list[:mid])
                node.right=bst(list[mid+1:])
                return temp
        mid=len(list)//2
        root=TreeNode()
        node=root
        node.val=list[mid]
        node.left=bst(list[:mid])
        node.right=bst(list[mid+1:])
    
        return root