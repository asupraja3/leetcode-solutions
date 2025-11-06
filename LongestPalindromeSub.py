class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around a potential palindrome center
        def expand_from_center(left: int, right: int) -> str:
            # Keep expanding while characters match and indices are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring found in the current expansion
            # (left+1 to right because the last expansion went one step too far)
            return s[left + 1:right]

        longest = ""  # To store the longest palindrome found

        # Iterate over each character in the string
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (single character center)
            palindrome1 = expand_from_center(i, i)
            
            # Case 2: Even-length palindrome (two-character center)
            palindrome2 = expand_from_center(i, i + 1)

            # Compare and store the longer palindrome between the two
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest  # Return the longest palindromic substring found
# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"