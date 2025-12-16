#Question 287: https://leetcode.com/problems/find-the-duplicate-number/description/
#Pattern: Two Pointers
#Time Complexity: O(n^2) Explained: We use a nested loop where the outer loop
# iterates through each element and the inner loop uses two pointers to compare
#Space Complexity: O(1) Explained: We are using only a constant amount of extra space
# for variables to store pointers and indices, regardless of input size.
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Length of the array
        n = len(nums)
        
        # Outer loop index
        i = 0

        # Iterate over the array using a shifting window
        while i < n:
            # 'left' starts at index 0
            left = 0
            
            # 'right' starts at i + 1 to avoid comparing the same index
            right = i + 1
            
            # Compare elements at 'left' and 'right'
            while right < n:
                # If two values are equal, we found the duplicate
                if nums[left] == nums[right]:
                    return nums[left]
                
                # Move both pointers forward together
                left += 1
                right += 1
            
            # Move to the next offset for comparison
            i += 1
        
        # If no duplicate is found (theoretically shouldn't happen
        # given problem constraints), return -1
        return -1
    
# --- Alternative Solution using Floyd's Tortoise and Hare Algorithm ---
#Pattern: Cycle Detection using Two Pointers
#Time Complexity: O(n) Explained: We traverse the array with two pointers,
# each moving at different speeds. Each element is processed at most once,
# leading to a linear time complexity.
#Space Complexity: O(1) Explained: We use a constant amount of extra space
# for variables to store pointers, regardless of input size.
from typing import List
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        # ---------------------------------------------------------
        # This solution uses Floyd's Tortoise and Hare algorithm
        # to detect a cycle in the array.
        #
        # Treat the array as a linked list:
        #   index -> nums[index]
        # The duplicate number creates a cycle.
        # ---------------------------------------------------------

        # Phase 1: Detect the cycle
        # 'slow' moves one step at a time
        # 'fast' moves two steps at a time
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]           # move slow pointer by 1 step
            fast = nums[nums[fast]]     # move fast pointer by 2 steps

            # When both pointers meet, a cycle is detected
            if slow == fast:
                break

        # Phase 2: Find the entry point of the cycle (duplicate number)
        # 'slow2' starts from the beginning of the list
        # 'slow' continues from the meeting point
        slow2 = 0

        while True:
            slow = nums[slow]           # move slow pointer by 1 step
            slow2 = nums[slow2]         # move slow2 pointer by 1 step

            # The node where both pointers meet is the duplicate number
            if slow == slow2:
                return slow

