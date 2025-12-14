#PAttern: Two Pointers
#Time Complexity: O(n) Explained: We traverse the list with two pointers, each moving towards
#  the center. Each element is processed at most once, leading to a linear time complexity.
#Space Complexity: O(n) Explained: We create a new list to store the squared values,
# which requires additional space proportional to the input size.
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Result array initialized with zeros
        # It will store the squared values in sorted order
        res = [0] * len(nums)

        # Two pointers:
        # 'left' starts at the beginning of the array
        # 'right' starts at the end of the array
        left = 0
        right = len(nums) - 1

        # We fill the result array from right to left
        # because the largest square will come from
        # either the leftmost or rightmost value
        for i in range(len(nums) - 1, -1, -1):
            
            # Compare absolute values since negative numbers
            # can produce large squares
            if abs(nums[left]) > abs(nums[right]):
                # Square the larger absolute value (left side)
                res[i] = nums[left] ** 2
                left += 1  # move left pointer inward
            else:
                # Square the larger absolute value (right side)
                res[i] = nums[right] ** 2
                right -= 1  # move right pointer inward
        
        # Return the sorted array of squares
        return res

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))  # Expected output: [0,1,9,16,100]
