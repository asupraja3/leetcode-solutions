#Question Link: https://leetcode.com/problems/backspace-string-compare/
#Time Complexity: O(N + M) where N and M are the lengths of strings s and t respectively.
#Space Complexity: O(N + M) for the stacks used to store the processed characters of both strings.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # Helper function to process a string by applying backspace operations
        def remove_characters(s):
            stack = []                     # Stack to build the final string
            
            for char in s:
                if char == '#' and stack:
                    stack.pop()            # Remove last character if backspace is found
                elif char != '#':
                    stack.append(char)     # Add normal characters to the stack
            
            return stack                   # Return the processed characters

        # Compare the processed results of both strings
        return remove_characters(s) == remove_characters(t)

# Example usage:
solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  # Output: True

