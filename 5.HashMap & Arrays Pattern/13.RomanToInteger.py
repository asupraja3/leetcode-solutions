#Pattern Used: Hash Map + String Traversal (Greedy Pattern)
#Why this pattern?: We need to map Roman numeral characters to their integer values
# and traverse the string to compute the total value based on Roman numeral rules.
# Time Complexity: O(n) where n is the length of the input string s. We traverse the string once.
# Space Complexity: O(1) as the size of the hash map is constant and does
class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0 
        # Loop through each character except the last one
        # because we compare s[i] with s[i+1]
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
            # If current symbol is smaller than the next symbol,
            # this is a subtractive case (like IV = 4, IX = 9).
            # So subtract its value from the total.
                total -= roman[s[i]]
            elif roman[s[i]] >= roman[s[i+1]]:
            # Otherwise, this is a normal additive case
            # (like VI = 6, XV = 15).
                total += roman[s[i]]
        # Add the value of the last character unconditionally.
        # It is always included since nothing comes after it.
        total+= roman[s[-1]]
        return total
        
#calls to the function can be made as follows:
sol = Solution()
print(sol.romanToInt("III"))  # 1994