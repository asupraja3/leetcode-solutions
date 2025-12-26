#Question URL: https://leetcode.com/problems/remove-linked-list-elements/
# Pattern Used: Linked List Traversal with Dummy Node
# Why this pattern?: Using a dummy node simplifies edge cases, such as removing the head node.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(1) as we are using constant extra space.
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Create a dummy node pointing to the head
        # This helps handle cases where the head itself needs to be removed
        ans = ListNode(0, head)
        
        # Pointer used to traverse the linked list
        dummy = ans

        # Traverse the list until the end
        while dummy:
            
            # Remove all consecutive nodes whose value equals 'val'
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next   # skip the node to be removed
            
            # Move to the next node
            dummy = dummy.next

        # Return the new head of the modified list
        return ans.next

# -----------------------------------------------------------------------------------------
#Another Approach without Dummy Node
# Time Complexity: O(n) where n is the number of nodes in the linked list.
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Create a dummy node to handle edge cases
        # (e.g., when the head node itself needs to be removed)
        temp = ListNode(0)
        temp.next = head

        # prev → points to the last node that is kept
        # curr → points to the current node being checked
        prev, curr = temp, head

        # Traverse the linked list
        while curr:
            
            # If current node's value matches 'val',
            # skip it by linking prev to curr.next
            if curr.val == val:
                prev.next = curr.next
            
            # Otherwise, move prev forward
            else:
                prev = curr
            
            # Move curr to the next node
            curr = curr.next

        # Return the new head of the modified list
        return temp.next
