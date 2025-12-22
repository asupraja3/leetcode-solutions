#Question URL: https://leetcode.com/problems/is-subsequence/
#Time Complexity: O(n) where n is the length of string t
#Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # sp → pointer for string s (subsequence)
        # tp → pointer for string t (main string)
        sp = tp = 0

        # Traverse both strings until one of them is fully processed
        while sp < len(s) and tp < len(t):
            
            # If characters match, move the subsequence pointer
            if s[sp] == t[tp]:
                sp += 1
            
            # Always move the pointer for t
            tp += 1

        # If we have matched all characters of s, it is a subsequence of t
        return sp == len(s)

#Brute Force Approach
#Time Complexity: O(n*m) where n is the length of string s and m is the length of string t
# Space Complexity: O(1)    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Index to track current position in t
        t_index = 0
        
        # Loop through each character in s
        for char in s:
            
            # Flag to check if current character is found in t
            found = False
            
            # Scan t starting from the last matched index
            while t_index < len(t):
                if t[t_index] == char:
                    found = True      # character matched
                    t_index += 1      # move to next position in t
                    break
                t_index += 1
            
            # If any character of s is not found in t
            if not found:
                return False
        
        # All characters of s were found in order
        return True

