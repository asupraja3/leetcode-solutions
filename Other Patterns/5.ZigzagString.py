#Pattern: Zigzag Conversion
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if there's only one row or the string is too short,
        # the zigzag pattern is just the string itself.
        if numRows == 1 or numRows >= len(s):
            return s
 
        # Create a list of strings for each row
        rows = [""] * numRows

        # Initialize current row and direction flag
        curr_row = 0
        going_down = False

        # Traverse each character in the input string
        for char in s:
            # Append the current character to its respective row
            rows[curr_row] += char
 
            # Change direction when we reach the top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
 
            # Move up or down depending on the current direction
            curr_row += 1 if going_down else -1

        # Join all rows to form the final converted string
        return "".join(rows)
     
# Example usage:
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"