# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # slow = fast = head
        # count = 0
        # while fast:
        #     fast = fast.next
        #     count+=1
        # if count == 0:
        #     return head
        # fast = head
        # k = k%count
        # # print(count,k)
        # while fast.next and k!=0: #count!=k:
        #     fast = fast.next
        #     k-=1

        # # print(count)
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # fast.next = head
        # head = slow.next
        # slow.next = None
        # return head

        # if head is empty or just one node
        if not head or not head.next:
            return head
        # count total number
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n+=1
        # print(n)
        # get relative k to rotate
        k = k%n
        if k == 0:                  # no need to rotate
            return head
        # where will be the new head be total - rotation 1
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        # print(new_tail.val)
        tail.next = head            # make circular
        head = new_tail.next        # set the new head
        new_tail.next = None        # break circle
        return head



        