

class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0               # Pointer to iterate through the string
        n = len(s)
        result = 0          # To store the final integer value
        sign = 1            # Default sign is positive

        # Step 1: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for optional sign (+ or -)
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1  # Move to next character after sign

        # Step 3: Convert consecutive digits into an integer
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Step 4: Handle overflow cases before they happen
            # result * 10 +digit <= INT_MAX
            if result > (INT_MAX - digit) // 10:
                # If overflow, return the clamped value based on sign
                return INT_MAX if sign == 1 else INT_MIN

            # Accumulate the digit into result
            result = result * 10 + digit
            i += 1

        # Step 5: Apply sign and return final result
        return sign * result
# Example usage:
solution = Solution()
print(solution.myAtoi("   -42"))        # Output: -42
print(solution.myAtoi("4193 with words")) # Output: 4193