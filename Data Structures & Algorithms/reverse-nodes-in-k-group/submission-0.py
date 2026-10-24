# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if K nodes are present
        if not self.hasKNodes(head, k):
            return head

        # Reverse 
        new_head, new_chunk_start = self.reverseChunk(head, k)

        head.next = self.reverseKGroup(new_chunk_start, k)

        return new_head

    def hasKNodes(self, head: Optional[ListNode], k: int) -> bool:
        cur = head
        for _ in range(k):
            if not cur:
                return False
            cur = cur.next
        return True

    def reverseChunk(self, head: Optional[ListNode], k: int):
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
        return prev, cur
