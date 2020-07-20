'''
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
#Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(-1)
        temp.next = head
        
        current = temp
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return temp.next
        
        
        
