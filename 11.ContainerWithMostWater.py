#Pattern: Two Pointers
#Time Complexity: O(n) Explained: We traverse the list with two pointers, each moving towards
#  the center. Each element is processed at most once, leading to a linear time complexity.
#Space Complexity: O(1) Explained: We use a constant amount of extra space for
# variables to store pointers and maximum area, regardless of input size.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer approach to find the maximum water container area.
        height: list of non-negative integers where each index i represents
                a vertical line at x = i with height = height[i].
        Returns the maximum area that can be formed between two lines.
        """

        # Initialize two pointers at the extremes of the array.
        left, right = 0, len(height) - 1

        # Track the best (maximum) area seen so far.
        max_area = 0

        # Move pointers toward each other until they meet.
        # At each step compute the area formed by the lines at left and right.
        while left < right:
            # Width is the horizontal distance between the two lines.
            width = right - left

            # The container's height is limited by the shorter line.
            h = height[left] if height[left] < height[right] else height[right]

            # Compute current area and update max_area if larger.
            current_area = h * width
            if current_area > max_area:
                max_area = current_area

            # Move the pointer pointing to the shorter line inward.
            # Reason: moving the taller line inward cannot increase the height
            # of the limiting side; only moving the shorter side might find a
            # taller boundary and thus possibly increase area despite reduced width.
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                # If they're equal, moving either pointer is fine. We can move both
                # or just one; here we move both to potentially skip useless checks.
                left += 1
                right -= 1

        return max_area


# --- Example usage / quick tests ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # expected 49
    print(sol.maxArea([1,1]))                # expected 1
    print(sol.maxArea([4,3,2,1,4]))          # expected 16
    print(sol.maxArea([1,2,1]))              # expected 2
# --- Example usage / quick tests ---

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(sol.maxArea([1,1]))  # 1