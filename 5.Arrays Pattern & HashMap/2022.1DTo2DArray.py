#Question Link: https://leetcode.com/problems/convert-1d-array-into-2d-array/
# Pattern: Arrays
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space Complexity: O(1) if we don't count the output array, otherwise O(m * n)

from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Total number of elements needed to fill an m x n matrix
        required_elements = m * n

        # If the number of elements in original does not match m * n,
        # it is impossible to construct the 2D array
        if len(original) != required_elements:
            return []

        # Resultant 2D array
        matrix = []

        # Index to track current position in the original array
        idx = 0

        # Build the 2D array row by row
        for _ in range(m):
            # Take next 'n' elements from original to form one row
            row = original[idx : idx + n]

            # Add the row to the matrix
            matrix.append(row)

            # Move index forward by 'n' elements
            idx += n

        return matrix
    
#Alternative Approach
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to form an m x n matrix
        if len(original) != m * n:
            return []

        # Use list comprehension to create the 2D array
        return [original[i * n:(i + 1) * n] for i in range(m)]
    
#Another Approach Using Iterator
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # If total elements do not match m * n,
        # it is impossible to construct the 2D array
        if m * n != len(original):
            return []

        # Resultant 2D array
        result = []

        # Temporary list to build each row
        current_row = []

        # Counter to track number of elements in the current row
        count = 0

        # Traverse through the original array
        for value in original:
            # Add current value to the row
            current_row.append(value)
            count += 1

            # Once we collect 'n' elements, finalize the row
            if count == n:
                result.append(current_row)
                current_row = []   # reset for next row
                count = 0          # reset counter

        return result

