# Definition for singly-linked list.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Dummy node helps handle edge cases like removing the head
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        # So the gap between fast and slow becomes n
        for _ in range(n):
            fast = fast.next

        # Move both fast and slow together until fast reaches the end
        # When fast hits the end, slow is just before the node to delete
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete the nth node (from end)
        slow.next = slow.next.next

        return dummy.next
    
# Example Usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)  # Output: [1,2,3,5]
# Function to print linked list for verification
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
print_linkedlist(new_head)