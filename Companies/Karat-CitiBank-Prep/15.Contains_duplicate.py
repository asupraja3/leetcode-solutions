def find_first_duplicate(log_entries):
    """
    # Given an array of log entry IDs, return the first ID that appears twice.
    """

    log_map= {}


    for num in log_entries:
        if num not in log_map:
            log_map[num] = 0
        if log_map[num] >=1:
            return num
        log_map[num] += 1

    return -1

def find_first_duplicate(log_entries):
    # 1. Edge case
    if len(log_entries) == 0:
        return -1
    log_map= set()
    for num in log_entries:
        if num in log_map:
            return num
        log_map.add(num)
    return -1

# --- Runnable Example ---
print(find_first_duplicate([101, 102, 101, 103]))  # Expected: 101
print(find_first_duplicate([1, 2, 3, 4, 5]))       # Expected: -1
print(find_first_duplicate([5, 3, 4, 3, 5]))       # Expected: 3
print(find_first_duplicate([]))                      # Expected: -1

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - We loop through the list only once.
      - Set lookup and insertion are O(1) on average.
    
    * Space Complexity: O(N)
      - We store up to N entries in the set in the worst case.
"""