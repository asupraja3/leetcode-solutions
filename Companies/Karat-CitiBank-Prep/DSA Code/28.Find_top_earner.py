def find_top_earner(entries):
    """
    # Given a 2D array where each row is [name, event_id, profit],
    # display each person's total profit and event count,
    # and return who had the most profit.
    """
    top_earner = ""
    emp_map = {}
    for parts in entries:
        emp, event, earn = parts[0], parts[1], int(parts[2])
        if emp not in emp_map:
            emp_map[emp] = {'earn':0, 'count':0}
        emp_map[emp]['earn']+=earn
        emp_map[emp]['count']+=1
    max_ear = 0
    print(emp_map)
    for emp,val in emp_map.items():

        if val['earn'] > max_ear:
            # print(val['earn'])
            max_ear = val['earn']
            top_earner = emp
    return top_earner






    return top_earner








# --- Runnable Example ---
entries = [
    ["Alice", "E101", "500"],
    ["Bob",   "E102", "300"],
    ["Alice", "E103", "200"],
    ["Bob",   "E104", "800"],
    ["Alice", "E105", "700"],
    ["Charlie","E106", "400"],
]

print("\nTop earner:", find_top_earner(entries))
# Output:
#   Alice - Profit: 1400 Events: 3
#   Bob - Profit: 1100 Events: 2
#   Charlie - Profit: 400 Events: 1
#
#   Top earner: Alice

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the number of entries.
      - Single pass to aggregate, single pass to find max.
    
    * Space Complexity: O(U)
      - U is the number of unique people in the dictionary.
"""