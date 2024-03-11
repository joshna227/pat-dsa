# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: #if not head:
            return 
        '''while head and head.val == val:
                head.next'''
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break
        temp = head
        while temp!=None and temp.next!=None:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
