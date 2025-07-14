'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''
#TC: O(n)
#SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0  # Initialize result to 0. This will hold the final decimal value.
        
        # Traverse through each node in the linked list
        while head:
            # Shift left the current result (multiply by 2) and add the current node's value
            res = 2 * res + head.val  # Binary number conversion logic
            
            # Move to the next node in the list
            head = head.next
        
        return res  # Return the final decimal result after the loop finishes
