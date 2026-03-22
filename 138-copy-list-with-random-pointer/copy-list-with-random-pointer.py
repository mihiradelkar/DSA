"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Questions:
        #  can the list be head be null?
        #  can the values be negative
        #  the random point to itself?
        #  can multiple node have random point to same node?
        
        # Approach 
        # Brute force: O(n^2) O(n)
        #  Pass 1: create all copy nodes, store them in an array by index
        #  For each node, walk the original list to figure out which index random points to
        #  Use that index to wire the copy
        # Optimal:
        #  pass one store acopy nodes in hashmap
        #  pass set next and random with hashmap with O(1) get

        if not head:
            return None
        list_map = {}
        curr = head 
        while curr:
            list_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head 
        while curr:                                             # map next and random for values in hash map
            if curr.next:
                list_map[curr].next = list_map[curr.next]       # stored[curr].next = stored[curr.next]
            if curr.random:
                list_map[curr].random = list_map[curr.random]
            curr = curr.next
        return list_map[head]
        
        # My method
        # dummy = copy = Node(0)
        # while curr:
        #     copy.next = list_map[curr] = Node(curr.val)
        #     list_map[curr].random = curr.random
        #     curr = curr.next
        #     copy = copy.next
        # curr = dummy.next 
        # while curr:
        #     if curr.random:
        #         curr.random = list_map[curr.random]
        #     curr = curr.next
        # return dummy.next