#Question Link: https://leetcode.com/problems/single-number/
# Pattern: Bit Manipulation & XOR
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(1) as we use a constant amount of extra space
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize result to 0
        # 0 is used because XOR with 0 returns the number itself
        res = 0

        # Iterate through each number in the list
        for n in nums:
            # XOR operation (^):
            # 1. a ^ a = 0        → same numbers cancel each other
            # 2. a ^ 0 = a        → XOR with 0 gives the number
            # 3. XOR is commutative and associative
            #    → order does not matter
            #
            # Since every number appears twice except one,
            # all duplicate numbers cancel out,
            # leaving only the single number
            res = res ^ n
        
        # res now contains the number that appears only once
        return res



#Brute Force Approach
# Pattern: Sorting & Pair Skipping
# Time Complexity: O(n log n) due to sorting step
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Sort the array so that duplicate numbers appear next to each other
        nums.sort()

        i = 0
        # Traverse the array
        while i < len(nums):
            # If the current element has a pair (same value next to it),
            # skip both elements
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 2
            else:
                # If no pair is found, this element appears only once
                return nums[i]
