#Questions: https://leetcode.com/problems/contains-duplicate/
# Pattern: HashMap & Arrays Pattern
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(n) for storing elements in the set
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False
    
#Pattern: Sorting & Adjacent Comparison
#Time Complexity: O(n log n) due to sorting step
#Space Complexity: O(1) if sorting in place, otherwise O(n)
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False