def two_sum(nums, target):
    """
    # Given an array of numbers and a target, find two numbers that add up to
    # the target and return their indices.
    """
    # 1. Dictionary to store seen numbers and their indices
    seen = {}
    
    # 2. Loop through and check for complement
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in seen:
            return [seen[comp], i]
        seen[nums[i]] = i
    
    # 3. Return empty list if no pair found
    return []


# --- Runnable Example ---
print(two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(two_sum([3, 2, 4], 6))         # Expected: [1, 2]

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - We loop through the list only once.
      - Dictionary lookup and insertion are O(1) on average.
    
    * Space Complexity: O(N)
      - We store up to N numbers in our dictionary in the worst case.
"""