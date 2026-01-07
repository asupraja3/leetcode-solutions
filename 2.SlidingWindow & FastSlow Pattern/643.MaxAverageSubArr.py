#Question Link: https://leetcode.com/problems/maximum-average-subarray-i/
#Pattern: Sliding Window
#Time Complexity: O(N)
#Space Complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Calculate the sum of the first window of size k
        # This serves as both the current sum and the initial maximum sum
        curr_sum = max_sum = sum(nums[:k])

        # Slide the window from index k to the end of the array
        for i in range(k, len(nums)):

            # Add the new element entering the window (nums[i])
            # Subtract the element leaving the window (nums[i - k])
            curr_sum += nums[i] - nums[i - k]

            # Update the maximum sum seen so far
            max_sum = max(curr_sum, max_sum)

        # Maximum average = maximum sum divided by window size k
        return max_sum / k
