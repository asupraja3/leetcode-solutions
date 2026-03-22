def user_access_range(logs):
    """
    # Part 1: For each user, find their earliest and latest timestamp
    # across all resource accesses.
    """
    if not logs:
        return {}

    user_map = {}
    for log in logs:
        vals = log.split(",")
        if vals[0] not in user_map:
            user_map[vals[0]] =[]
        user_map[vals[0]].append(int(vals[2]))

    # print(user_map)
    result = {}
    for user,times in user_map.items():
        # times.sort()
        # if user not in result:
        #     result[user] = []
        result[user]=[min(times),max(times)]
        # result[user].append()

    return result



# --- Runnable Example ---
logs = [
    "user1,resourceA,100",
    "user1,resourceB,200",
    "user1,resourceA,350",
    "user2,resourceA,120",
    "user2,resourceC,500",
    "user1,resourceA,150",
    "user2,resourceA,250",
    "user2,resourceA,300",
    "user3,resourceB,800",
    "user3,resourceB,150"
]

# Part 1
print("=== User Access Ranges ===")
ranges = user_access_range(logs)
for user in ranges:
    print(user, ":", ranges[user])
# Expected:
#   user1 : [100, 350]
#   user2 : [120, 500]
#   user3 : [150, 800]

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the total number of logs.
      - We loop through the logs once to build the dictionary. 
      - min() and max() scan through each user's times once. The sum of all these smaller scans equals N.
    
    * Space Complexity: O(N)
      - We store every access time in our user_map dictionary.
"""