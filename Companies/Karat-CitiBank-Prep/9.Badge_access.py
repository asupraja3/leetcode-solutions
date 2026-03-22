def find_mismatches(records):
    """
    # Find employees who entered without exiting and exited without entering.
    """
    # 1. Use sets to easily avoid duplicates and keep Time Complexity at O(N)
    enter_wo_exit = set()
    exit_wo_enter = set()

    # 2. Dictionary to track current status (0 = outside, 1 = inside)
    list_log = {}

    # 3. Process each log entry
    for user, log in records:
        if user not in list_log:
            list_log[user] = 0
            
        if log == 'enter':
            if list_log[user] == 1:
                # Already inside but trying to enter again
                enter_wo_exit.add(user)
            else:
                # Update status to inside
                list_log[user] = 1
                
        else: # log == 'exit'
            if list_log[user] == 0:
                # Already outside but trying to exit
                exit_wo_enter.add(user)
            else:
                # Update status to outside
                list_log[user] = 0
                
    # 4. Check the dictionary for anyone left inside at the end of the records
    for user, val in list_log.items():
        if val == 1:
            enter_wo_exit.add(user)
            
    # 5. Convert the sets back to lists for the final output
    return [list(enter_wo_exit), list(exit_wo_enter)]

# --- Runnable Example ---
records1 = [
    ["Paul", "enter"], ["Pauline", "exit"], ["Paul", "enter"],
    ["Paul", "exit"], ["Martha", "exit"], ["Joe", "enter"],
    ["Martha", "enter"], ["Steve", "enter"], ["Martha", "exit"],
    ["Jennifer", "enter"], ["Joe", "enter"], ["Curtis", "exit"],
    ["Curtis", "enter"], ["Joe", "exit"], ["Martha", "enter"],
    ["Martha", "exit"], ["Jennifer", "exit"], ["Joe", "enter"],
    ["Joe", "enter"], ["Martha", "exit"], ["Joe", "exit"],
    ["Joe", "exit"]
]

result = find_mismatches(records1)
print("Enter without exit:", result[0])
print("Exit without enter:", result[1])
# Expected:
# Enter without exit: ["Steve", "Curtis", "Paul", "Joe"]
# Exit without enter: ["Martha", "Pauline", "Curtis", "Joe"]
# Note: Output order may vary slightly because sets are unordered, which is fine!

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the number of records.
      - We loop through the records once, then loop through the dictionary once.
      - Dictionary and Set lookups/insertions are O(1) on average.
    
    * Space Complexity: O(U)
      - U is the number of UNIQUE users in the records.
      - We store up to U unique names across our dictionary and sets.
"""