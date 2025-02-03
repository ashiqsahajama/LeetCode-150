# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        m = 0
        while curr:
            m+=1
            curr = curr.next
        curr = dummy
        for _ in range(m-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

