#Question URL: https://leetcode.com/problems/permutation-in-string/
#Pattern: Sliding Window and HashMap
#Time Complexity: O(N), where N is the length of s2
# Explained: Each character is added and removed from the sliding window at most once. 
# s2_count and s1_count comparisons take O(1) time since the character set is fixed 
# (26 lowercase letters).
#Space Complexity: O(1), since the character set is limited to lowercase English letters,
# the hashmap size is bounded by a constant.
from collections import defaultdict
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # If s1 is longer than s2, s2 cannot contain any permutation of s1
        if len(s1) > len(s2):
            return False

        # Frequency map for characters in s1
        s1_count = collections.defaultdict(int)
        # Frequency map for the current sliding window in s2
        s2_count = collections.defaultdict(int)  

        # Build frequency counts for:
        # - entire s1
        # - first window of s2 with length equal to s1
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1 

        # If the first window is already a permutation of s1
        if s1_count == s2_count:
            return True  
        
        # Left pointer of the sliding window
        left = 0

        # Slide the window over s2 starting from index len(s1)
        for right in range(len(s1), len(s2)):

            # Add the new character entering the window (right side)
            s2_count[s2[right]] += 1

            # Remove the character leaving the window (left side)
            s2_count[s2[left]] -= 1

            # If frequency becomes 0, remove the character from the map
            # to keep the maps comparable
            if s2_count[s2[left]] == 0:
                s2_count.pop(s2[left])
            
            # Move the left pointer forward
            left += 1

            # Check if current window is a permutation of s1
            if s1_count == s2_count:
                return True 
        
        # No permutation of s1 found in s2
        return False
