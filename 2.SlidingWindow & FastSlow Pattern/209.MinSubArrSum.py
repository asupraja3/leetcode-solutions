#Question Link: https://leetcode.com/problems/minimum-size-subarray-sum/
#Pattern: Sliding Window and Two Pointers
#Time Complexity: O(N), where N is the length of the input array nums 
# Explained: Each element is added and removed from the sliding window at most once.
#Space Complexity: O(1)
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Stores the minimum length of a valid subarray found so far
        # Initialized to infinity so any valid length will be smaller
        min_len = float("inf")
        
        # Left pointer of the sliding window
        left = 0
        
        # Sum of the current window
        cur_sum = 0

        # Right pointer expands the sliding window
        for right in range(len(nums)):
            
            # Add the current element to the window sum
            cur_sum += nums[right]

            # Shrink the window while the current sum meets or exceeds target
            while cur_sum >= target:
                
                # Update minimum length if the current window is smaller
                min_len = min(min_len, right - left + 1)
                
                # Remove the leftmost element to shrink the window
                cur_sum -= nums[left]
                
                # Move the left pointer forward
                left += 1
        
        # If no valid subarray was found, return 0; otherwise return min_len
        return min_len if min_len != float("inf") else 0
