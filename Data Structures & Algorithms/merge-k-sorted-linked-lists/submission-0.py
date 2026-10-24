# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        return self.div_n_con(lists, 0 , len(lists) - 1)

    def div_n_con(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        # Base case
        if left == right:
            return lists[left]

        mid = left + (right - left) // 2
        
        left_res = self.div_n_con(lists, left, mid)
        right_res = self.div_n_con(lists, mid + 1, right)

        return self.mergeTwoLists(left_res, right_res)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        tail.next = l1 or l2

        return dummy.next

        