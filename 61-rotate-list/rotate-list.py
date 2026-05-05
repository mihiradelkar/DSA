# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        count = 0
        while fast:
            fast = fast.next
            count+=1
        if count == 0:
            return head
        fast = head
        k = k%count
        # print(count,k)
        while fast.next and k!=0: #count!=k:
            fast = fast.next
            k-=1

        # print(count)
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        



        