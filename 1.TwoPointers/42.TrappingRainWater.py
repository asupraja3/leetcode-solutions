#Question Link: https://leetcode.com/problems/trapping-rain-water/
#Pattern: Two Pointers
#Time Complexity: O(N), where N is the length of the input array height
# Explained: We traverse the height array twice to fill max_left and max_right arrays,
# and then once more to calculate the total trapped water.
#Space Complexity: O(N), where N is the length of the input array height
#Explained: We use two additional arrays max_left and max_right of size N to store
#  the maximum heights to the left and right of each index.
#We could optimize space to O(1) by using two pointers without additional arrays, but this implementation uses O(N) space for clarity.

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the total amount of rainwater that can be trapped.
        """

        n = len(height)
        if n == 0:
            return 0

        # Arrays to store maximum height to the left and right of each index
        max_left = [0] * n
        max_right = [0] * n

        # Two pointers for traversing from left and right
        left, right = 0, n - 1

        # Variables to track max height seen so far from left and right
        left_max = 0
        right_max = 0

        # Build max_left and max_right in a single pass
        for _ in range(n):
            # Update left maximum
            left_max = max(left_max, height[left])
            max_left[left] = left_max

            # Update right maximum
            right_max = max(right_max, height[right])
            max_right[right] = right_max

            left += 1
            right -= 1

        total_water = 0

        # Calculate trapped water at each index
        for i in range(n):
            # Water trapped is min(max_left, max_right) - current height
            total_water += min(max_left[i], max_right[i]) - height[i]

        return total_water
