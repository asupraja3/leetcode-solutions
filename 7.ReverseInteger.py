#Patttern: Reverse Integer
#Time Complexity: O(log10(n)) - The time complexity is O(log10(n)) because the 
# number of digits in the integer n determines the number of iterations needed to reverse it. 
# Each iteration processes one digit.
#Space Complexity: O(1) - The space complexity is O(1) because we
# are using a constant amount of space regardless of the input size. 
# The variables used to store the sign, reversed number, 
# and digit do not scale with the size of the input integer.

class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range limits
        # These are the boundaries for a signed 32-bit integer.
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Determine the sign of the input number.
        # If x is negative, store -1; otherwise store +1.
        sign = -1 if x < 0 else 1

        # Work only with the absolute value of x to simplify reversal logic.
        x = abs(x)

        # Initialize the reversed number as 0.
        reversed_num = 0

        # Loop until all digits are processed.
        while x != 0:
            digit = x % 10      # Extract the last digit (remainder when divided by 10)
            x //= 10            # Remove the last digit from x (integer division by 10)

            # Before multiplying by 10 and adding the new digit,
            # check whether doing so would overflow the 32-bit signed integer limit.
            # This condition ensures:
            # reversed_num * 10 + digit <= INT_MAX
            if reversed_num > (INT_MAX - digit) // 10:
                return 0        # Return 0 if reversing would overflow

            # Safely add the extracted digit to the reversed number
            reversed_num = reversed_num * 10 + digit

        # Reapply the original sign (positive or negative) and return the result.
        return sign * reversed_num

# Example usage:
solution = Solution()
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))   # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (overflow case)