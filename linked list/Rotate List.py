# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next == None or k==0:
            return head
        len=1
        current=head
        #for computing length od linked list
        while current.next:
            current=current.next
            len=len+1
        current.next=head
        k=k%len
        rotate=len-k
        while rotate:
            current=current.next
            rotate=rotate-1
        head=current.next
        current.next=None
        return head
