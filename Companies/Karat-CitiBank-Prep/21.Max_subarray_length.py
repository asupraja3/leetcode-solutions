def find_max_length(nums1, nums2):
    """
    # Find the maximum length of a subarray that appears in both arrays.
    # e.g. [1,2,3,2,1] and [3,2,1,4,7] -> 3 ([3,2,1])
    """
    max_length = 0

    # 1. Loop through every starting index in nums1
    for i in range(len(nums1)):
        
        # 2. Loop through every starting index in nums2
        for j in range(len(nums2)):
            
            # 3. Use a counter instead of a list to track the current match length
            curr_len = 0
            curr_i, curr_j = i, j
            
            # 4. While elements match, keep moving both pointers forward
            while curr_i < len(nums1) and curr_j < len(nums2) and nums1[curr_i] == nums2[curr_j]:
                curr_len += 1
                curr_i += 1
                curr_j += 1

                # Update the global maximum if this match is the longest we've seen
                if max_length < curr_len:
                    max_length = curr_len

    return max_length


# --- Runnable Example ---
print(find_max_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
# Expected: 3

print(find_max_length([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
# Expected: 5

print(find_max_length([1, 2, 3], [4, 5, 6]))
# Expected: 0

"""
    Complexity Analysis:
    
    * Time Complexity: O(N * M * min(N, M))
      - N is the length of nums1, M is the length of nums2.
      - We have two outer loops (N * M), and the inner `while` loop can run up to the length of the shortest array. 
      - (Note for interviews: This is slower than the DP approach, but perfectly valid as a first working solution).
    
    * Space Complexity: O(1)
      - By switching from building a list to using a simple `curr_len` counter, we use constant space regardless of array size.
"""