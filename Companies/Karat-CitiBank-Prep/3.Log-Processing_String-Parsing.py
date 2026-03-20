def find_most_frequent_user(logs):
    """
    # Part 1: Given a list of user IDs and their login timestamps, 
    # find the user who logged in the most.
    # Format: logs = [["user_id", "timestamp"], ...]
    """
    user_counts = {}
    
    # 1. Count every login for each user
    for user, timestamp in logs:
        if user not in user_counts:
            user_counts[user] = 0
        user_counts[user] += 1
        
    # 2. Find the user with the highest count
    most_frequent = None
    max_count = 0
    
    for user, count in user_counts.items():
        if count > max_count:
            max_count = count
            most_frequent = user
            
    return most_frequent

print(find_most_frequent_user([["user1", "2021-01-01 10:00:00"], 
["user2", "2021-01-01 10:05:00"], ["user1", "2021-01-01 10:10:00"], ["user3", "2021-01-01 10:15:00"],
["user1", "2021-01-01 10:25:00"], ["user3", "2021-01-01 10:30:00"], ["user2", "2021-01-01 10:35:00"],
]))  
# Output: ["user1"]


"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the total number of logs. We look at every log exactly once to count them, 
      and then loop through the unique users to find the max.
      
    * Space Complexity: O(U)
      - U is the number of unique users. We store one count per unique user in our dictionary.
"""

""" 
    Edge Cases to Consider:
    1. An empty list of logs (should return None).
    2. All users have the same number of logins (should return any one of them).
    3. Logs with invalid formats (should handle gracefully, but we assume input is well-formed).
    4. Logs with timestamps in different formats (should handle gracefully, but we assume input is well-formed).
    5. Logs with missing user IDs or timestamps (should handle gracefully, but we assume input is well-formed).
    6. A very large number of logs (should still perform efficiently).
"""

# -------------------------------------------------------------------------------------------------

def find_longest_active_period(logs, target_user):
    """
    # Part 2: Given a list of user IDs, their login/logout timestamps, and a target user ID,
    # find the longest continuous active period for that user.
    # Format: logs = [["user_id", int(timestamp), "action"], ...]
    """
    max_period = 0
    start_time = None
    
    # 1. Scan the logs once
    for user, timestamp, action in logs:
        if user == target_user:
            if action == "login":
                # Save the start of the current session
                start_time = timestamp
            elif action == "logout" and start_time is not None:
                # Calculate duration and update the record
                duration = timestamp - start_time
                if duration > max_period:
                    max_period = duration
                
                # Reset start_time to prepare for the next session
                start_time = None
                
    return max_period

# Calling the function with your example data:
log_data = [
    ["user1", 1609459200, "login"],  # 12:00:00 AM
    ["user1", 1609462800, "logout"], # 01:00:00 AM (Duration: 3600s)
    ["user1", 1609466400, "login"],  # 02:00:00 AM
    ["user1", 1609470000, "logout"], # 03:00:00 AM (Duration: 3600s)
    ["user2", 1609459200, "login"],
    ["user2", 1609462800, "logout"]
]

print(find_longest_active_period(log_data, "user1"))
# Output: 3600

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
        - N is the total number of logs. We look at every log exactly once to find the longest active period.   
    * Space Complexity: O(1)
        - We only use a few variables to keep track of the current session and the maximum period
         regardless of the number of logs.
"""

# ---------------------------------------------------------------------------------------------------

def most_common_3_step_sequence(logs):
    """
    # Part 3: Find the most common "3-step" sequence of pages visited.
    # Format: logs = [["user_id", "page_name"], ...]
    """
    user_history = {}
    
    # 1. Build an ordered list of pages for each user
    for user, page in logs:
        if user not in user_history:
            user_history[user] = []
        user_history[user].append(page)
        
    sequence_counts = {}
    
    # 2. Find every 3-step sequence for every user
    for user, pages in user_history.items():
        # Stop if they haven't visited at least 3 pages
        if len(pages) < 3:
            continue
            
        # Slide a window across their page history
        for i in range(len(pages) - 2):
            # Grab exactly 3 pages
            seq = (pages[i], pages[i+1], pages[i+2])
            
            if seq not in sequence_counts:
                sequence_counts[seq] = 0
            sequence_counts[seq] += 1
    print(sequence_counts) # {('pageA', 'pageB', 'pageC'): 2} 
    # 3. Find the most frequent sequence
    most_common_seq = None
    max_count = 0
    
    for seq, count in sequence_counts.items():
        if count > max_count:
            max_count = count
            most_common_seq = seq
            
    return most_common_seq 
# or return max(sequence_count, key=sequence_count.get)

# Example usage:
log_data = [ 
    ["user1", "pageA"],
    ["user1", "pageB"],
    ["user1", "pageC"],
    ["user2", "pageA"],
    ["user2", "pageB"],
    ["user2", "pageC"]
]
print(most_common_3_step_sequence(log_data))
# Output: ("pageA", "pageB", "pageC")

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the number of logs. Grouping the histories takes O(N). Sliding the 3-step window across those histories also scales linearly with the number of logs.
      
    * Space Complexity: O(N)
      - In the worst case, we store every single log entry in the `user_history` dictionary, and the `sequence_counts` dictionary will also scale with the log size.
"""

# ----------------------------------------------------------------------------------------------------


