#Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Pattern Used: Linked List Traversal with Dummy Node
# Why this pattern?: Using a dummy node simplifies edge cases, such as removing the head node.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are using constant extra space.
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node pointing to the head
        # This simplifies edge cases, especially when the first node is a duplicate
        temp = ListNode(0, head)

        # left  → points to the last unique node kept in the list
        # right → traverses the linked list
        left, right = temp, head

        # Variable to store the previously seen value
        # Initialized to a value outside the problem constraints
        val = -200

        # Traverse the linked list
        while right:

            # If current node value is the same as the previous value,
            # it is a duplicate and should be removed
            if right.val == val:
                left.next = left.next.next   # skip the duplicate node
            
            # Otherwise, current node is unique
            else:
                left = right                 # move left pointer forward
            
            # Update previously seen value
            val = right.val

            # Move to the next node
            right = right.next
        
        # Return the head of the modified list without duplicates
        return temp.next
    
# -----------------------------------------------------------------------------------------
#Another Approach without Dummy Node
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are using constant extra space.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Pointer to traverse the linked list
        curr = head

        # Traverse until the end of the list
        while curr and curr.next:
            
            # If current node and next node have the same value,
            # skip the next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            
            # Otherwise, move to the next node
            else:
                curr = curr.next

        # Return the modified list
        return head

