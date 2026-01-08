#Question Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Pattern Used: Two Pointers
# Why this pattern?: We use two pointers moving at different speeds to find the middle node.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are using only two pointers.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize both pointers at the head node
        # slow → moves one step
        # fast → moves two steps
        fast = slow = head

        # Traverse the list until fast reaches the end
        while fast and fast.next:
            
            # Move fast pointer by two nodes
            fast = fast.next.next
            
            # Move slow pointer by one node
            slow = slow.next

        # If fast is not None, the list has even number of nodes
        # Move slow one more step to return the second middle
        # if fast:
            # slow = slow.next

        # slow now points to the middle node
        return slow

