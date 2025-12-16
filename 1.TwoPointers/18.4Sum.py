#Question 18: https://leetcode.com/problems/4sum/description/
#Pattern: Two Pointers Technique after Sorting
#Why this pattern?: We need to find unique quadruplets that sum to a target value.
#Time Complexity: O(n^3) where n is the number of elements in nums.
#Sorting the array takes O(n log n) and the two-pointer approach inside two nested loops takes O(n^2).
#Space Complexity: O(1) if we don't count the output space, as we are using only a
# constant amount of extra space.
class Solution:
    def fourSum(self, nums, target):
        # Sort nums so that:
        # 1. We can avoid duplicates easily
        # 2. We can use two-pointer technique for the inner search
        nums.sort()
        n = len(nums)
        result = []

        # First loop: pick the 1st number of the quadruplet
        for i in range(n):

            # Skip duplicate values for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second loop: pick the 2nd number of the quadruplet
            for j in range(i + 1, n):

                # Skip duplicate values for the second position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Now we will find the remaining two numbers using two pointers
                left = j + 1
                right = n - 1

                # Two-pointer approach for the last two numbers
                while left < right:

                    # Calculate the sum of the selected four numbers
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if four_sum == target:
                        # We found a valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move left pointer forward
                        left += 1
                        # Skip duplicate values for left pointer
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Move right pointer backward
                        right -= 1
                        # Skip duplicate values for right pointer
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif four_sum < target:
                        # Sum is too small → increase it by moving left pointer
                        left += 1
                    else:
                        # Sum is too large → decrease it by moving right pointer
                        right -= 1

        return result
# Example usage:
solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(solution.fourSum([2,2,2,2,2], 8))        # Output: [[2, 2, 2, 2]]
