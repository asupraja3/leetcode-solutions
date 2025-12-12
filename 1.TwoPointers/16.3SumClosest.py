#Pattern: Two Pointers Technique after Sorting
#Why this pattern?: We need to find a triplet whose sum is closest to a given target.
#Time Complexity: O(n^2) where n is the number of elements in nums.
#Sorting the array takes O(n log n) and the two-pointer approach takes O(n^2).
#Space Complexity: O(1) if we don't count the output space, as we are using only a
# constant amount of extra space.
class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the array so we can apply the two-pointer technique.
        nums.sort()
        n = len(nums)

        # Initialize the closest sum with something large.
        # We can use the sum of the first 3 elements as a starting point.
        closest_sum = nums[0] + nums[1] + nums[2]

        # Iterate through each element and treat it as the first number of the triplet.
        for i in range(n):

            # Two-pointer setup:
            # left starts just after i
            # right starts at the end of the list
            left = i + 1
            right = n - 1

            # Move left and right pointers inward to find best possible combination
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If current sum is closer to target than our stored closest_sum, update it
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on how current_sum compares to target
                if current_sum < target:
                    # Sum is too small → increase by moving left pointer to the right
                    left += 1
                elif current_sum > target:
                    # Sum is too big → decrease by moving right pointer to the left
                    right -= 1
                else:
                    # Exact match found → this is the closest possible sum
                    return current_sum

        # After checking all combinations, return the closest sum found
        return closest_sum

Sol = Solution()
print(Sol.threeSumClosest([-1,2,1,-4], 1))  # Expected output: 2