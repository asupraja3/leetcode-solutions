#Question Link: https://leetcode.com/problems/sliding-window-maximum/
#Pattern: Sliding Window and Deque
#Time Complexity: O(N), where N is the length of the input array nums
# Explained: Each element is added and removed from the deque at most once.
#Space Complexity: O(K), where K is the size of the sliding window,
# the deque can hold at most K elements.
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque()   # Stores indices of elements
        result = []        # Stores max of each window

        # -------- First Loop: Build the first window --------
        for i in range(k):
            # Remove smaller elements from the back
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # Add current index
            window.append(i)

        # Max of the first window
        result.append(nums[window[0]])

        # -------- Second Loop: Slide the window --------
        for right in range(k, len(nums)):
            # Remove elements outside the window
            if window[0] < right - k + 1:
                window.popleft()

            # Remove smaller elements from the back
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            # Add current index
            window.append(right)

            # Front of deque is the maximum
            result.append(nums[window[0]])

        return result



#Another Approach: 
#Does not work optimally for large inputs due to O(n*k) time complexity

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0                      # Left index of the sliding window
        max_values = []               # Stores the maximum of each window
        window_elements = []          # Stores elements of the current window

        # Step 1: Build the first window of size k
        for i in range(k):
            window_elements.append(nums[i])

        # Step 2: Find max of the first window
        current_max = max(window_elements)
        max_values.append(current_max)

        # Step 3: Slide the window across the array
        for right in range(k, len(nums)):
            # Add the new element entering the window
            window_elements.append(nums[right])

            # Remove the element leaving the window
            window_elements.remove(nums[left])
            left += 1

            # Find max of the current window
            current_max = max(window_elements)
            max_values.append(current_max)

        return max_values
