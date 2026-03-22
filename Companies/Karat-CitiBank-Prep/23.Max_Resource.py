def max_resource_in_window(logs, window=300):
    """
    # Part 2: Find which resource was accessed the most times
    # within any 5-minute (300 second) window.
    # Return the resource, count, and list of timestamps in that window.
    """
    # 1. Dictionary to group timestamps by resource
    by_resource = {}
    
    for log in logs:
        parts = log.split(",")
        resource = parts[1]
        ts = int(parts[2])
        
        if resource not in by_resource:
            by_resource[resource] = []
        by_resource[resource].append(ts)


    max_count = 0
    max_times = []
    max_resource = ""

    for res,times in by_resource.items():
        times.sort()
        left = 0

        for right in range(0,len(times)):

            while times[right] - times[left] > window:
                left+=1
            
            curr_count = right - left + 1

            if curr_count > max_count:
                max_count = curr_count
                max_resource = res
                max_times = []
                for k in range(left,right+1):
                    max_times.append(times[k])

    return [max_resource,max_count,max_times]
        


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

# Part 2
print("\n=== Max Resource in 5-min Window ===")
resource, count, times = max_resource_in_window(logs)
print("Resource:", resource, "Count:", count, "Times:", times)
