
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize two pointers at the head
        # slow → moves one step at a time
        # fast → moves two steps at a time
        slow = fast = head

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:

            slow = slow.next          # move slow pointer by 1
            fast = fast.next.next     # move fast pointer by 2

            # If both pointers meet, a cycle is detected
            if slow == fast:
                break
        else:
            # If loop exits normally, no cycle exists
            return None

        # Phase 2: Find the starting node of the cycle
        # Reset fast pointer to the head
        fast = head

        # Move both pointers one step at a time
        # The node where they meet is the cycle entry point
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        # Return the node where the cycle begins
        return slow

# Brute Force Approach using HashSet
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(n) for storing visited nodes in the hash set.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head
        
        while current:
            # If we have seen this node before, it's the start of the cycle
            if current in visited:
                return current
            
            # Mark the current node as visited
            visited.add(current)
            
            # Move to the next node
            current = current.next
        
        # If we reach the end, there is no cycle
        return None