class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        p = head

        while(p.next):
            if p.next in s:
                return True
            s.add(p.next)
        return False
