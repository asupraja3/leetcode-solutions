def pivot_index(nums):
    """
    # Find the index where the sum of elements to the left
    # equals the sum of elements to the right.
    """
    # pivot = -1

    for i in range(len(nums)):
        # pivot = nums[i]
        left_sum,right_sum=0,0

        for j in range(i-1,-1,-1):
            left_sum+=nums[j]

        for k in range(i+1,len(nums)):
            right_sum+=nums[k]

        
        if right_sum == left_sum:
            return i

        # 4. No pivot found
    return -1


def pivot_index1(nums):

    total_sum = sum(nums)
    curr_sum = 0
    for i in range(len(nums)):
        
        if total_sum- curr_sum - nums[i] == curr_sum:
            return i
        curr_sum +=nums[i]
    return[i]

# --- Runnable Example ---
print(pivot_index([1, 7, 3, 6, 5, 6]))  # Expected: 3 (left=11, right=11)
print(pivot_index([1, 2, 3]))             # Expected: -1 (no pivot)
print(pivot_index([2, 1, -1]))            # Expected: 0 (left=0, right=0)

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - First pass to compute total sum, second pass to find pivot.
    
    * Space Complexity: O(1)
      - We only use two variables: total and left.
"""