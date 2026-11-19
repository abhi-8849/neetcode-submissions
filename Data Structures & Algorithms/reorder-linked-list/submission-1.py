# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)

        slow = head
        fast = head

        # get middle/ Split in 2 halves
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        # Reverse L2
        prev = None
        cur = l2

        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        l1 = head
        l2 = prev

        dummy = ListNode()
        tail = dummy
        tail.next = l1

        # Merge 2 lists
        while l2:
            nxtl1 = l1.next
            nxtl2 = l2.next

            l1.next = l2
            l2.next = nxtl1

            l1 = nxtl1
            l2 = nxtl2
