#Question 75: https://leetcode.com/problems/sort-colors/description/
#Pattern Used: Counting Sort / Two Pointers
#Why this pattern?: We need to sort an array with a limited range of values (0, 1, 2).
# Time Complexity: O(n) where n is the number of elements in nums. We make
# two passes through the array: one for counting and one for overwriting.
# Space Complexity: O(1) as we are using only a constant amount of extra space
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)                  # Length of the input array

        count = [0] * 3                # Count occurrences of 0s, 1s, and 2s

        # First pass: count how many times each color appears
        for i in range(n):
            count[nums[i]] += 1

        index = 0                      # Pointer to overwrite nums in sorted order

        # Second pass: overwrite nums based on the counts
        for i in range(3):             # i represents the color (0, 1, 2)
            for _ in range(count[i]):  # Repeat for the number of times color i appears
                nums[index] = i        # Place the color at the current index
                index += 1             # Move to the next position



# Bubble Sort Approach
# Time Complexity: O(n^2) where n is the number of elements in nums.
# Space Complexity: O(1) as we are using only a constant amount of extra space.

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        # n = len(nums)                     # Get the length of the array

        # Outer loop controls the number of passes
        # After each pass, the largest element moves to the end
        for i in range(n):

            left = 0                      # Pointer to the current element
            right = 1                     # Pointer to the next element

    # Compare adjacent elements until the unsorted part is exhausted
            while right < n - i:

        # Swap if elements are in the wrong order
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]

            left += 1                 # Move left pointer forward
            right += 1                # Move right pointer forward
