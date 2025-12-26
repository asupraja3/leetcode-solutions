#Question URL: https://leetcode.com/problems/palindrome-linked-list/
# Pattern Used: Two Pointers
# Why this pattern?: We use two pointers to compare values from both ends of the list.
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(n) for storing node values in an array.

from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # List to store all node values from the linked list
        arr = []
      
        # Traverse the linked list and copy values into the array
        while head:
            arr.append(head.val)
            head = head.next

        # Initialize two pointers for palindrome check
        # left  → start of the array
        # right → end of the array
        left, right = 0, len(arr) - 1

        # Compare values from both ends moving toward the center
        while left < right:

            # If mismatch found, it is not a palindrome
            if arr[left] != arr[right]:
                return False

            # Move pointers inward
            left += 1
            right -= 1
        
        # All values matched successfully
        return True

#Another Approach using Stack
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(n) for storing node values in a stack.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Stack to store all node values from the linked list
        stack = []
      
        # Traverse the linked list and push values onto the stack
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        # Traverse the linked list again to compare with stack values
        current = head
        while current:
            # Pop value from stack and compare with current node's value
            if current.val != stack.pop():
                return False
            current = current.next
        
        # All values matched successfully
        return True