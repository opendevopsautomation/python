# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        lst[k-1],lst[-k]=lst[-k],lst[k-1]
        node=ListNode()
        head=node
        i=0
        while i< len(lst):
            node.val=lst[i]
            if i != len(lst)-1:
                temp=ListNode()
                node.next=temp
                node=node.next
            i+=1
        return head 

'''Optimization in the above program'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        lst=[]
        temp=head
        while temp:
            lst.append(temp)
            temp=temp.next
        lst[k-1].val,lst[-k].val=lst[-k].val,lst[k-1].val

        return head     