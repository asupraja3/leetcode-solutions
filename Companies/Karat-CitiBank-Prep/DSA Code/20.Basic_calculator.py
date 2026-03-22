def calculate(s):
    """
    # Basic Calculator - evaluate string with +, -, (, ) and spaces.
    # e.g. "(1+(4+5+2)-3)+(6+8)" = 23
    """
    # 1. Initialize variables for tracking our math
    stack = []
    total = 0
    current_num = 0
    sign = 1  # 1 means '+', -1 means '-'

    # 2. Loop through each character exactly once
    for char in s:
        
        # Build a multi-digit number (e.g., '1' and '0' becomes 10)
        if char.isdigit():
            current_num = (current_num * 10) + int(char)
            
        # When we hit a plus, finalize the previous number, add to total, set sign to positive
        elif char == '+':
            total += sign * current_num
            current_num = 0
            sign = 1
            
        # When we hit a minus, finalize the previous number, add to total, set sign to negative
        elif char == '-':
            total += sign * current_num
            current_num = 0
            sign = -1
            
        # When hitting '(', pause current math: save total and sign to stack, reset them
        elif char == '(':
            stack.append(total)
            stack.append(sign)
            total = 0
            sign = 1
            
        # When hitting ')', finish inner math, and combine with the paused math from the stack
        elif char == ')':
            total += sign * current_num
            current_num = 0
            
            # The top of the stack is the sign just before the '('
            total *= stack.pop()
            # The next item is the total from before the '('
            total += stack.pop()

    # 3. Add any lingering number at the very end of the string to the total
    total += sign * current_num

    return total

# --- Runnable Example ---
print(calculate("1 + 1"))                # Expected: 2
print(calculate(" 2-1 + 2 "))            # Expected: 3
print(calculate("(1+(4+5+2)-3)+(6+8)"))  # Expected: 23
print(calculate("10 + (3 - 1)"))         # Expected: 12
print(calculate("-(3+2) + 1"))           # Expected: -4

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the length of the string.
      - We loop through each character exactly once.
      - Stack operations are O(1).
    
    * Space Complexity: O(N)
      - Stack can grow up to N in the worst case with heavily nested parentheses.
"""