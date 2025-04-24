# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        prev = None
        while l1.next != null:
            next = l1.next
  
            l1.next = prev            
            next.next = l1.val
            prev = l1.val
            l1.val = next

        while l2.next != null:
            next = l2.next

            l2.next = prev            
            next.next = l2.val
            prev = l2.val
            l2.val = next

                    