#Question 15: https://leetcode.com/problems/3sum/description/
# Pattern: Two Pointers Technique after Sorting
# Why this pattern?: We need to find unique triplets that sum to zero.
# Time Complexity: O(n^2) where n is the number of elements in nums.
# Sorting the array takes O(n log n) and the two-pointer approach takes O(n^2).
# Space Complexity: O(1) if we don't count the output space, as we are using only a 
# constant amount of extra space.


class Solution:
    def threeSum(self, nums):
        # Sort the array because:
        # 1. It helps avoid duplicate triplets easily.
        # 2. It allows using a two-pointer approach efficiently.
        nums.sort()

        result = []       # To store all unique triplets
        n = len(nums)

        # Iterate through the array, treating nums[i] as the first number of the triplet
        for i in range(n):

            # If nums[i] is the same as the previous value, skip it.
            # This prevents forming triplets with the same first number twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer technique:
            # left starts right after i
            # right starts at the end of the list
            left = i + 1
            right = n - 1

            # Move the left and right pointers inward
            while left < right:

                # Calculate the sum of the three numbers
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Valid triplet found
                    result.append([nums[i], nums[left], nums[right]])

                    # Move left pointer to the next value
                    left += 1
                    # Skip duplicate values for left pointer to avoid repeated triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Move right pointer to the previous value
                    right -= 1
                    # Skip duplicate values for right pointer as well
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # If sum is too small, move left pointer to increase the sum
                    left += 1

                else:
                    # If sum is too large, move right pointer to decrease the sum
                    right -= 1

        # Return all unique triplets that sum to zero
        return result

# Example usage:
solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
