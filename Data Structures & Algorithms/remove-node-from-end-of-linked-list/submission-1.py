# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = p1
        index = 0
        while p2.next is not None:
            index += 1
            p2 = p2.next
        if n == index + 1:
            return head.next
        for i in range(index - n + 1):
            p2 = p1
            p1 = p1.next
        p2.next = p1.next
        return head


