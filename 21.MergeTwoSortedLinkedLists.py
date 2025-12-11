# Pattern Used: Linked List + Two Pointers Pattern
# Why this pattern?: We need to merge two sorted linked lists into one sorted linked list
# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively
# Space Complexity: O(1) as we are not using any extra space except for a few pointers

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Convert Python list to linked list
def list_to_linkedlist(arr):
    dummy = ListNode()
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# Initialize a dummy node to help with the merged list
        dummy = ListNode()
# Use a pointer to track the current end of the merged list
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
# Attach the smaller node to the merged list and move the pointer forward
                current.next = list1
                list1 = list1.next
            else:
# Attach the smaller node to the merged list and move the pointer forward
                current.next = list2
                list2 = list2.next
            current = current.next
# At the end of the loop, at least one of the lists is exhausted. Attach the 
# remaining part of the other list.
# Since the lists are sorted, we can simply point to the non-null list.       
        if list1:
            current.next = list1
        else: 
            current.next = list2
        
        return dummy.next
    
# Example Usage:
list1 = list_to_linkedlist([1,2,4])
list2 = list_to_linkedlist([1,3,4])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)  # Output: [1,1,2,3,4,4]


