#Question Link: https://leetcode.com/problems/longest-repeating-character-replacement/
#Pattern: Sliding Window and HashMap
#Time Complexity: O(N), where N is the length of the input string s  
# Explained: Each character is added and removed from the sliding window at most once.
# The max frequency calculation takes O(1) time since the character set is fixed (26
# lowercase letters).
#Space Complexity: O(1), since the character set is limited to lowercase English letters,
# the hashmap size is bounded by a constant.

def characterReplacement(self, s: str, k: int) -> int:
    
    left = 0                  # Left pointer of the sliding window
    freq = {}                 # Dictionary to store frequency of characters in the window
    max_len = 0               # Stores the maximum valid window length found

    # Expand the window using the right pointer
    for right in range(len(s)):
        # Add the current character to the frequency map
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Find the maximum frequency of any character in the current window
        max_freq = max(freq.values())

        # If replacements needed > k, shrink the window from the left
        # (window size - most frequent character count gives replacements needed)
        if (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1    # Remove the left character from the window
            left += 1             # Move the left pointer forward

        # Update the maximum window size
        max_len = max(max_len, right - left + 1)

    # Return the length of the longest valid substring
    return max_len
