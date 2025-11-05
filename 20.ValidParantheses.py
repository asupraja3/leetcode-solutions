# Pattern Used: Stack (LIFO - Last In, First Out)
# Why this pattern?: We need to keep track of opening parentheses and ensure they are
# properly closed in the correct order, which is efficiently handled by a stack data structure.
# Time Complexity: O(n) where n is the length of the input string s. We traverse the string once.
# Space Complexity: O(n) in the worst case for the stack, when all characters are opening parentheses.
# We push all opening parentheses onto the stack. If the string is valid, the stack will be empty 
# at the end.
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if  mapping[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack