#Question Link: https://leetcode.com/problems/fruit-into-baskets/
#Pattern: Sliding Window and Two Pointers and HashMap
#Time Complexity: O(N), where N is the length of the input array fruits
# Explained: Each element is added and removed from the sliding window at most once.
#Space Complexity: O(1), since the fruit types are limited to 2, the hashmap size is bounded by a constant.
from typing import List
import collections


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        # Stores the maximum number of fruits collected (answer)
        max_fruits_collected = 0
        
        # Left pointer of the sliding window
        left = 0
        
        # Dictionary to store fruit type counts inside the current window
        fruit_count = collections.defaultdict(int)

        # Right pointer expands the sliding window
        for right in range(len(fruits)):
            
            # Add the current fruit to the window
            fruit_count[fruits[right]] += 1

            # Shrink the window if more than 2 fruit types are present
            while len(fruit_count) > 2:
                
                # Remove the fruit at the left pointer from the window
                fruit_count[fruits[left]] -= 1
                
                # If a fruit type count becomes zero, remove it completely
                if fruit_count[fruits[left]] == 0:
                    fruit_count.pop(fruits[left])
                
                # Move the left pointer forward to shrink the window
                left += 1

            # Update the maximum window size (total fruits collected)
            #max of max fruits and current_window_size  
            max_fruits_collected = max(max_fruits_collected, right - left + 1)

        return max_fruits_collected
