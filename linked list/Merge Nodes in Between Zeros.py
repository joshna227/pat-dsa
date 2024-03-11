# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=write=ListNode(0)
        s=0
        while head:
            if head.val!=0:
                s+=head.val
                head=head.next
            else:
                write.next=ListNode(s)
                write=write.next
                head=head.next
                s=0
        return dummy.next.next
