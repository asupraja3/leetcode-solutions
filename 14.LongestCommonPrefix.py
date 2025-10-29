#Pattern Used: Horizontal Scanning / Prefix Reduction Pattern
#Why this pattern?: We need to iteratively reduce the common prefix by comparing
# it with each string in the array.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

#calls to the function can be made as follows:
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # ""