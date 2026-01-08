#Question Link: https://leetcode.com/problems/linked-list-cycle/
# Pattern Used: Two Pointers (Floyd’s Cycle-Finding Algorithm)
# Why this pattern?: We use two pointers moving at different speeds to detect a cycle.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are using only two pointers.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
                # Initialize two pointers at the head of the linked list
        # left  → moves one step at a time (slow pointer)
        # right → moves two steps at a time (fast pointer)
        right = head
        left = head
        
        # Traverse the list while the fast pointer can move ahead
        while right and right.next:
            
            # Move fast pointer by two nodes
            right = right.next.next
            
            # Move slow pointer by one node
            left = left.next

            # If both pointers meet, a cycle exists
            if right == left:
                return True

        # If fast pointer reaches the end, no cycle exists
        return False

# Example Usage:
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Creates a cycle for testing
solution = Solution()
print(solution.hasCycle(head))  # Output: True


#Brute Force Approach using HashSet
#Time Complexity: O(n) where n is the number of nodes in the linked list.
#Space Complexity: O(n) for storing visited nodes in the hash set.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        
        while current:
            # If we have seen this node before, there is a cycle
            if current in visited:
                return True
            
            # Mark the current node as visited
            visited.add(current)
            
            # Move to the next node
            current = current.next
        
        # If we reach the end of the list, there is no cycle
        return False