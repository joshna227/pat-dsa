# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=ListNode(0)
        temp.next=head
        fast=slow=head
        for i in range(k-1):
            fast=fast.next
        temp1=fast
        while fast.next:
            fast=fast.next
            slow=slow.next
        temp1.val,slow.val=slow.val,temp1.val
        return temp.next