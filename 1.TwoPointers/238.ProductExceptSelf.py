#Question Link: https://leetcode.com/problems/product-of-array-except-self/
#Patttern: Two Pointers & HashMap
#Time Complexity:  O(n * m) where m is the number of unique elements
#Space Complexity: O(m) for the hashmap storing counts of unique elements

from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input array
        leng = len(nums)
        
        # Create a dictionary to store the count of each unique number in nums
        hmap = defaultdict(int)
        for i in range(leng):
            hmap[nums[i]] += 1   # Increment the count of nums[i] in the map
        
        # Debug print to see the counts of each number (can remove in production)
        print(hmap)
        
        # Initialize the answer array
        answer = []
        
        # Variable to store the product for each element
        prod = 1
        
        # Loop through each element in the original array
        for i in range(leng):
            
            # For each element, calculate the product of all other elements
            for key, value in hmap.items():
                # If the current key is the same as nums[i], exclude one occurrence
                if nums[i] == key:
                    value = value - 1
                
                # Multiply the key raised to its (possibly adjusted) count
                prod *= (key ** value)
            
            # Append the product to the answer list
            answer.append(prod)
            
            # Reset prod for the next iteration
            prod = 1
        
        # Return the final list where each element is the product of all other elements
        return answer

#Optimized Solution: 
# Time Complexity: O(n), Explanation: We traverse the array three times (once for left 
# products, once for right products, and once for final multiplication).
# Space Complexity: O(1), Explanation: We use the output array to store the results
# We do not use any additional space that scales with input size.
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an array nums, returns an array answer such that
        answer[i] is the product of all elements in nums except nums[i].
        
        Constraints:
        - No division allowed
        - O(n) time complexity
        - O(1) extra space (output array does not count)
        
        Example:
        nums = [1, 2, 3, 4]
        Step 1 (left products):
            answer = [1, 1, 2, 6]  
            Explanation:
            answer[0] = 1 (no elements to the left)
            answer[1] = 1 (product of [1])
            answer[2] = 1*2 = 2 (product of [1,2])
            answer[3] = 1*2*3 = 6 (product of [1,2,3])
        
        Step 2 (multiply by right products):
            right_product = 1 initially
            answer[3] *= 1  => 6
            answer[2] *= 4  => 8
            answer[1] *= 12 => 12
            answer[0] *= 24 => 24
        
        Final answer: [24, 12, 8, 6]
        """
        
        n = len(nums)
        
        # Step 1: Initialize answer array with 1s
        # answer[i] will eventually contain the product of all elements to the left of i
        answer = [1] * n
        
        left_product = 1  # Running product of elements to the left
        for i in range(n):
            answer[i] = left_product  # Store product of all elements to the left
            left_product *= nums[i]   # Update left_product to include nums[i]
        
        # Step 2: Multiply by right products
        right_product = 1  # Running product of elements to the right
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product  # Multiply by product of elements to the right
            right_product *= nums[i]    # Update right_product to include nums[i]
        
        return answer


# Example usage:
# sol = Solution()
# print(sol.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
# print(sol.productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]
