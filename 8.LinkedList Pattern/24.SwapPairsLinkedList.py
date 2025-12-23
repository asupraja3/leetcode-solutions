#Question Link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Pattern: Linked List Manipulation
# Why this pattern?: We need to manipulate the pointers of linked list nodes to 
# swap pairs.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are only using a few pointers and not any extra 
# data structures.


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list.
        # This helps handle edge cases (like swapping the first two nodes)
        dummy = ListNode(0, head)
        
        # 'prev' will always point to the node **before the current pair**
        # 'curr' points to the first node of the current pair we want to swap
        prev, curr = dummy, head

        # Traverse the list in pairs
        while curr and curr.next:
            # 'second' is the second node in the pair
            second = curr.next
            
            # 'nextpair' is the node after the current pair
            # We need to save it because 'curr.next' will change during swap
            nextpair = curr.next.next 

            # Step 1: Point the second node to the first node to swap the pair
            second.next = curr

            # Step 2: Connect the first node to the rest of the list (nextpair)
            curr.next = nextpair

            # Step 3: Connect the previous part of the list to the new first node of this pair (second)
            prev.next = second

            # Step 4: Move 'prev' to the end of the swapped pair (curr)
            prev = curr

            # Step 5: Move 'curr' to the start of the next pair
            curr = nextpair

        # Return the new head (dummy.next), which may be different from original head
        return dummy.next
