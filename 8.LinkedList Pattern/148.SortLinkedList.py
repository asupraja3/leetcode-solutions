# Question URL: https://leetcode.com/problems/sort-list/
# Pattern Used: Merge Sort on Linked List
# Time Complexity: O(N log N) where N is the number of nodes in the linked list
# Space Complexity: O(log N) due to recursion stack space


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case:
        # If the list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list
        # Use slow and fast pointers:
        # - slow moves one step at a time
        # - fast moves two steps at a time
        # When fast reaches the end, slow will be at the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        mid = slow.next        # start of right half
        slow.next = None       # break the list into two parts

        # Step 2: Recursively sort both halves
        left = self.sortList(head)   # sort left half
        right = self.sortList(mid)   # sort right half

        # Step 3: Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        # Dummy node to simplify merging logic
        dummy = ListNode(0)
        curr = dummy

        # Compare nodes from both lists and attach the smaller one
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1      # attach l1 node
                l1 = l1.next        # move l1 forward
            else:
                curr.next = l2      # attach l2 node
                l2 = l2.next        # move l2 forward
            curr = curr.next        # move current pointer

        # Attach any remaining nodes from either list
        # (only one of l1 or l2 can be non-empty here)
        curr.next = l1 or l2

        # Return the head of the merged sorted list
        return dummy.next
