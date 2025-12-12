#Pattern Used: Horizontal Scanning / Prefix Reduction Pattern
#Why this pattern?: We need to iteratively reduce the common prefix by comparing
# it with each string in the array.
# Time Complexity: O(S) where S is the sum of all characters in all strings.
# In the worst case, all strings are the same and we compare each character of each string
# Space Complexity: O(1) as we are using only a constant amount of space.
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # If the list is empty, no common prefix exists
        if not strs:
            return ""

    # Start by assuming the entire first string is the common prefix
        prefix = strs[0]

    # Compare the current prefix with each of the remaining strings
        for s in strs[1:]:

        # Reduce the prefix until the current string starts with it
        # Example: prefix = "flower", s = "flow" → trims to "flow"
            while not s.startswith(prefix):
            # Remove the last character from prefix
                prefix = prefix[:-1]

            # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""

    # Return the final prefix after checking all strings
        return prefix


#calls to the function can be made as follows:
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # ""