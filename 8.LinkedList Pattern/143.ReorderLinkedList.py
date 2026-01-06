#Question link: https://leetcode.com/problems/reorder-list/
#Pattern: Linked List
#Time Complexity: O(N)
#Space Complexity: O(1)
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the linked list in-place to:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        """

        # Base case:
        # If the list is empty or has only one node, no reordering is needed
        if not head or not head.next:
            return head

        # ---------------------------------------------------
        # 1. Find the middle of the linked list
        # ---------------------------------------------------
        # Use slow and fast pointers:
        # - slow moves one step at a time
        # - fast moves two steps at a time
        # When fast reaches the end, slow will be at the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        # first half: head → ... → slow
        # second half: slow.next → ... → end
        second = slow.next
        slow.next = None     # terminate first half
        node = None          # will be the head of reversed second half

        # ---------------------------------------------------
        # 2. Reverse the second half of the list
        # ---------------------------------------------------
        # Standard linked list reversal
        while second:
            tmp = second.next     # store next node
            second.next = node    # reverse the pointer
            node = second         # move head of reversed list
            second = tmp          # move to next node

        # ---------------------------------------------------
        # 3. Merge the two halves alternately
        # ---------------------------------------------------
        # first: pointer for first half
        # second: pointer for reversed second half
        first = head
        second = node

        while second:
            # Save next pointers before overwriting
            tmp1, tmp2 = first.next, second.next

            # Link nodes alternately
            first.next = second
            second.next = tmp1

            # Move both pointers forward
            first, second = tmp1, tmp2
