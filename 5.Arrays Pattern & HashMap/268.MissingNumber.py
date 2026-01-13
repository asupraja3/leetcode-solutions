#Question Link: https://leetcode.com/problems/missing-number/
# Pattern: Summation & Index Difference
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(1) as we use a constant amount of extra space
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # len(nums) gives 'n' where numbers should be in the range [0, n]
        # enumerate(nums) provides (index, value) pairs
        
        # For a perfect array containing all numbers from 0 to n,
        # the sum of (index - value) for all elements would be 0.
        # Since one number is missing, this difference accumulates
        # and the final result equals the missing number.
        
        return len(nums) + sum(i - num for i, num in enumerate(nums))

#Another Approach:
# Pattern: Summation Formula
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(1) as we use a constant amount of extra space
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n is the total count including the missing number
        n = len(nums)

        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Actual sum of elements present in the array
        actual_sum = sum(nums)

        # The difference gives the missing number
        return expected_sum - actual_sum
