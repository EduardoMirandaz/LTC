# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list_node = ListNode()
        head = list_node

        while list1 and list2:

            if(list1.val < list2.val):
                list_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list_node.next = ListNode(list2.val)
                list2 = list2.next
            
            list_node = list_node.next
        
        if(list1):
            list_node.next = list1
        elif(list2):
            list_node.next = list2

        return head.next

