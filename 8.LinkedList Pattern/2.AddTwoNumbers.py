#Question Link: https://leetcode.com/problems/add-two-numbers/
# Pattern Used: Linked List Traversal with Carry Handling
# Why this pattern?: We need to traverse two linked lists simultaneously, adding corresponding digits
# along with any carry from the previous addition.
# Time Complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m, n)) for the new linked list that stores the result.
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Another Approach without using extra variable 'tail'
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode(0)
        carry = 0 
        current = dummy
        while l1 != None or l2 != None or carry!=0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + carry
            carry = sum // 10
            current.next = ListNode(sum%10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

#calls to the function can be made as follows:
sol = Solution()
# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents the number 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents the number 465
result = sol.addTwoNumbers(l1, l2)  # Should represent the number

#Another Approach
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy node to simplify result list construction
        dummy = ListNode()
        
        # Pointer to build the result linked list
        res = dummy

        # Variables to store sum and carry
        total = 0
        carry = 0

        # Continue while there are nodes in l1 or l2 or a remaining carry
        while l1 or l2 or carry:
            
            # Start with carry from the previous addition
            total = carry

            # Add value from l1 if available
            if l1:
                total += l1.val
                l1 = l1.next

            # Add value from l2 if available
            if l2:
                total += l2.val
                l2 = l2.next
            
            # Current digit is total modulo 10
            num = total % 10
            
            # Carry for the next iteration
            carry = total // 10
            
            # Append the computed digit to the result list
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        # Return the head of the newly formed linked list
        return res.next
