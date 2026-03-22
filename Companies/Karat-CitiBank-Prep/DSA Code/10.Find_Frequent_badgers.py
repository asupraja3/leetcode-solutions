def find_frequent_badgers(badge_times):
    """
    # Find employees who badged in 3+ times within any one-hour window.
    # Return the earliest such window for each employee.
    """
    # 1. Dictionary to group all times by employee
    times_by = {}
    for name, time in badge_times:
        if name not in times_by:
            times_by[name] = []
        times_by[name].append(int(time))
    
    # 2. For each employee, sort times and check sliding windows
    result = {}
    
    for name in times_by:
        times = times_by[name]
        times.sort()
        
        # 3. Use two pointers to find a window of 60 mins with 3+ entries
        for i in range(len(times)):
            window = [times[i]]
            
            for j in range(i + 1, len(times)):
                if times[j] - times[i] <= 100:  # within 1 hour (e.g. 800 to 900)
                    window.append(times[j])
                else:
                    break
            
            # If we found 3+ in this window, store it and move to next person
            if len(window) >= 3:
                result[name] = window
                break
    
    return result


# --- Runnable Example ---
badge_times = [
    ["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
    ["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
    ["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
    ["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
    ["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
    ["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
    ["Jennifer", "5"], ["Chloe", "1510"], ["Chloe", "1540"],
    ["Chloe", "1560"], ["Jennifer", "1505"], ["Jennifer", "1515"],
    ["Jennifer", "1535"], ["Chloe", "1520"], ["Chloe", "1530"],
    ["Jose", "1620"],
]

result = find_frequent_badgers(badge_times)
for name in result:
    print(name, ":", result[name])

# Expected output (earliest 1-hour window with 3+ badges):
# Jose : [830, 835, 855]
# Chloe : [1510, 1520, 1530]
# Jennifer : [1505, 1515, 1535]
# Paul : [1315, 1355, 1405]

"""
    Complexity Analysis:
    
    * Time Complexity: O(N + E * K log K)
      - N is total number of badge records.
      - E is the number of unique employees.
      - K is the max number of badges per employee (for sorting).
      - Grouping takes O(N). For each employee we sort O(K log K)
        then scan with two pointers O(K).
    
    * Space Complexity: O(N)
      - We store all badge times grouped by employee in a dictionary.
"""