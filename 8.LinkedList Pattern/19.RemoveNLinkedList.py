#Question Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Pattern Used: Two Pointers (Fast and Slow)
#time Complexity: O(L) where L is the length of the linked list
#space Complexity: O(1)
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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Create a dummy node pointing to the head
        # This helps handle edge cases like removing the first node
        dummy = ListNode(0, head)

        # Step 1: Calculate the total length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Find the position of the node to remove from the start
        # (length - n) gives the index of the node BEFORE the one to remove
        pos = length - n

        # Step 3: Traverse to the node just before the target node
        curr = dummy
        for _ in range(pos):
            curr = curr.next

        # Step 4: Remove the nth node from the end
        curr.next = curr.next.next

        # Return the modified list
        return dummy.next
