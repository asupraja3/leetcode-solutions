#Question 713: https://leetcode.com/problems/subarray-product-less-than-k/description/
#Pattern Used: Two Pointers / Sliding Window
#Why this pattern?: We need to find contiguous subarrays with a product less than k.
# Time Complexity: O(n) where n is the number of elements in nums. Each element is processed at most twice.
# Space Complexity: O(1) as we are using only a constant amount of space.
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # If k is 0 or 1, no positive product can be less than k
        if k <= 1:
            return 0

        left = 0              # Left pointer of the sliding window
        product = 1           # Product of elements inside the window
        count = 0             # Total number of valid subarrays

        # Move the right pointer through the array
        for right in range(len(nums)):
            # Include the current element in the product
            product *= nums[right]

            # If product becomes invalid (>= k), shrink window from the left
            while product >= k:
                product //= nums[left]  # Remove left element from product
                left += 1               # Move left pointer forward

            # All subarrays ending at 'right' and starting from
            # any index between 'left' and 'right' are valid
            count += right - left + 1

        # Return total count of valid subarrays
        return count




#Brute Force Approach
#time Complexity: O(n^2) where n is the number of elements in nums.
#Space Complexity: O(1) as we are using only a constant amount of space.
class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if prod < k:
                    count += 1
                else:
                    break
        return count
        