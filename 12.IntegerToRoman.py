#Pattern: Greedy Algorithm + Hash Map
#Why this pattern?: We need to build the Roman numeral representation
# by greedily using the largest possible symbols first, which is efficiently
# achieved using a predefined mapping of integer values to Roman symbols.
# Time Complexity: O(1) Explained: The number of Roman numeral symbols is fixed,
# so the loop runs a constant number of times regardless of the input size.
# Space Complexity: O(1) Explained: We use a fixed amount of extra space for
# the list of value-symbol pairs and the output list, independent of input size.

class Solution:
    def intToRoman(self, num: int) -> str:

        roman = []  # List to accumulate Roman numeral parts

        # List of (value, symbol) pairs, ordered from largest to smallest.
        # Includes both standard and subtractive forms.
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        # Loop through each Roman numeral value in descending order
        for value, symbol in value_symbols:

            # Optimization: stop early if the number becomes zero
            if num == 0:
                break

            # Determine how many times the Roman symbol fits into num
            # Example: num = 3749 → 3749 // 1000 = 3 → append "MMM"
            remainder = num // value

            # Subtract the equivalent value added to Roman representation
            num = num - (remainder * value)

            # Append symbol repeated 'remainder' times
            # Example: remainder = 3, symbol = 'M' → "MMM"
            roman.append(remainder * symbol)

        # Join all parts into the final Roman numeral string
        return "".join(roman)


# Testing
sol = Solution()
print(sol.intToRoman(3749))   # expected "MMMDCCXLIX"
# print(sol.intToRoman(4))    # expected "IV"
