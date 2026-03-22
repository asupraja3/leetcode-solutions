def board_game(start, dice_rolls, teleporters):
    """
    # Given a start position, dice rolls, and teleporters,
    # return all positions you land on.
    """
    # 1. Build the teleporter dictionary cleanly
    tele_map = {}
    for tel, val in teleporters:
        tele_map[tel] = val

    # 2. Initialize tracking variables using the actual 'start' parameter
    visited = set()
    curr_val = start
    visited.add(curr_val)

    # 3. Process each dice roll
    for num in dice_rolls:
        # Move forward by the dice roll amount
        curr_val += num
        
        # 4. Check if the CURRENT POSITION (not the roll) is a teleporter.
        # Using 'while' handles the edge case of landing on chained teleporters.
        while curr_val in tele_map:
            curr_val = tele_map[curr_val]
            
        # Record the final landing spot for this turn
        visited.add(curr_val)

    return visited

# --- Runnable Example ---
start = 0
dice_rolls = [3, 4, 2, 6, 1]
teleporters = [(3, 15), (7, 12), (20, 5)]

print(board_game(start, dice_rolls, teleporters))
# Walkthrough:
#   Start: 0
#   Roll 3 -> land on 3 -> teleport to 15
#   Roll 4 -> land on 19
#   Roll 2 -> land on 21
#   Roll 6 -> land on 27
#   Roll 1 -> land on 28
# Expected: {0, 15, 19, 21, 27, 28}

"""
    Complexity Analysis:
    
    * Time Complexity: O(N + T)
      - N is the number of dice rolls, T is the number of teleporters.
      - Dictionary lookups and set insertions are O(1) on average.
      - (Assuming teleporters do not form an infinite loop).
    
    * Space Complexity: O(N + T)
      - The set stores up to N+1 positions, and the dictionary stores T teleporters.
"""