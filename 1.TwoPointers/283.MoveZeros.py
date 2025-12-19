#Question: https://leetcode.com/problems/move-zeroes/
#Time Complexity: O(N) where N is the length of the input array.
#Space Complexity: O(1) since we are modifying the array in place without using extra space.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modify nums in-place to move all zeros to the end
        while maintaining the relative order of non-zero elements.
        """

        left = 0  # Points to the position where the next non-zero element should be placed

        # Traverse the array using 'right' pointer
        for right in range(len(nums)):

            # If the current element is non-zero
            if nums[right] != 0:

                # Swap the current non-zero element with the element at 'left'
                # This pushes zeros toward the right and keeps non-zero order intact
                nums[right], nums[left] = nums[left], nums[right]

                # Move 'left' forward to the next position
                left += 1


#---------------------------------------------------------------------------------------------

#Approach2: Get the count of zeros first, then fill in non-zeros and zeros accordingly.
# Time Complexity: O(N) where N is the length of the input array.
#Space Complexity: O(1) since we are modifying the array in place without using extra space.

n = len(nums)   # Total number of elements in the array

# Initialize count of zeros
count = 0

# ❌ Incorrect approach (generator expression without sum)
# count = (count + 1 for i in nums if i == 0)
# This creates a generator, not an integer

# ✅ Correct way: count how many zeros are in the array
count = nums.count(0)

index = 0  # Points to the position where the next non-zero element should go

# First pass:
# Move all non-zero elements to the front of the array
# while maintaining their relative order
for i in range(len(nums)):
    if nums[i] != 0:
        nums[index] = nums[i]
        index += 1

# Second pass:
# Fill the remaining positions with zeros
for _ in range(count):
    nums[index] = 0
    index += 1

# ---------------------------------------------------------------------------------------------
#Approach3: Bubble up zeros to the end by repeated swapping.(Does not work for large arrays)
# Time Complexity: O(N^2) in the worst case due to nested loops.

# Repeat the process n times to gradually push all zeros to the end
for i in range(n):

    left = 0          # Pointer to the current position to check for zero
    right = 1         # Pointer to the next element used for swapping

    # Shrink the range after each pass because the largest elements
    # (or zeros, depending on logic) settle at the end
    while right < n - i:

        # If the element at 'left' is zero, swap it with the next element
        # so zeros move one step toward the right
        if nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]

        # Move both pointers one step to the right
        left += 1
        right += 1


