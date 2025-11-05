#Pattern: Sliding Window
#Time Complexity: O(n), where n is the length of the string. Each character is processed at most 
#   twice (once by the right pointer and once by the left pointer). Total operations ≤ 2n
# 
#At first glance, it seems nested → could be O(n²) But each character is added to the set at
#  most once and removed at most once.
# So across the entire string, the inner loop executes at most n time
#Space Complexity: O(min(m, n)), where m is the size of the character set and n is the length
# of the string. In the worst case, the sliding window will contain all unique characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the left pointer of the sliding window and the max length found
        left = max_length = 0
        
        # Use a set to store characters currently in the sliding window
        char_set = set()
        
        # Iterate over each character in the string using the right pointer
        for right in range(len(s)):
            
            # If the character is already in the set, shrink the window from the left
            # until the duplicate character is removed
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character
                left += 1                 # Move left pointer to the right
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the maximum length of substring found so far
            max_length = max(max_length, right - left + 1)
        
        # Return the length of the longest substring without repeating characters
        return max_length