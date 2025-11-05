# Pattern Used: Hashing / HashMap Pattern
# Why this pattern?:We need to quickly check if a number’s complement (i.e., target - current) 
# already exists — and hashmaps allow O(1) lookups.
# Time Complexity: O(n) where n is the number of elements in nums
# Space Complexity: O(n) in the worst case for storing elements in the hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

