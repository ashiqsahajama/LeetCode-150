# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prevL = dummy
        curr = head
        for i in range(left-1):
            prevL = curr
            curr = curr.next
        p = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = p
            p,curr = curr,temp
        prevL.next.next = curr
        prevL.next = p
        return dummy.next
