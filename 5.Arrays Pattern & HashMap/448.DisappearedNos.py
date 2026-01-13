#Question Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Pattern: In-Place Marking & Two Passes
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(1) as we use a constant amount of extra space
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # First pass:
        # Use the value of each element as an index and mark that index as visited
        # We mark visited indices by making the value at that index negative
        
        for i in range(len(nums)):
            # Convert the current number to an index (1-based → 0-based)
            idx = abs(nums[i]) - 1
            
            # If the value at this index is positive, mark it as visited
            if nums[idx] > 0:
                nums[idx] *= -1

        # List to store numbers that never appeared in the array
        res = []
        
        # Second pass:
        # Any index that still has a positive value was never visited
        for i in range(len(nums)):
            if nums[i] > 0:
                # i + 1 because indices are 0-based but numbers are 1-based
                res.append(i + 1)
        
        return res


#Alternative Approach:
# Pattern: Set & Range Comparison
# Time Complexity: O(n) where n is the number of elements in the input array
# Space Complexity: O(n) for storing elements in the set
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Create a set of all numbers present in the array
        num_set = set(nums)
        
        # Find all numbers in the range [1, n] that are not in the set
        res = [i for i in range(1, n + 1) if i not in num_set]
        
        return res

#Brute-force Approach:
# Pattern: Nested Loops & Direct Search
# Time Complexity: O(n^2) due to nested loops for searching each number
# Space Complexity: O(1) as we use a constant amount of extra space
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        res = []

        for n in range(1, len(nums) + 1):
            if n not in numbers:
                res.append(n)
        
        return res

