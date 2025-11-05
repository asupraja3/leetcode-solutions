# Pattern Used: Linked List Traversal with Carry Handling
# Why this pattern?: We need to traverse two linked lists simultaneously, adding corresponding digits
# along with any carry from the previous addition.
# Time Complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m, n)) for the new linked list that stores the result.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode(0)
        tail = dummy
        carry = 0 
        while l1 != None or l2 != None or carry!=0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + carry
            carry = sum // 10
            newNode = ListNode(sum%10)
            tail.next = newNode
            tail = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next