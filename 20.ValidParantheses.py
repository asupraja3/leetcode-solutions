# Pattern Used: Stack (LIFO - Last In, First Out)
# Why this pattern?: We need to keep track of opening parentheses and ensure they are
# properly closed in the correct order, which is efficiently handled by a stack data structure.

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