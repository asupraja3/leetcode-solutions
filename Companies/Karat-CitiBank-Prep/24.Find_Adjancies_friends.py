def find_adjacencies(employees, friendships):
    """
    # Given employees and friendships, build adjacency list.
    # Friendships are bi-directional.
    """

    emp_map = {}
    for emp in employees:
        val = emp.split(",")
        val0,val1 = int(val[0].strip()), val[1].strip()
        emp_map[val0] = val1
    print(emp_map)
    result = {}
    f_map = {}
    for f in friendships:
        ids = f.split(",")
        ids0,ids1 = int(ids[0].strip()), int(ids[1].strip())
        if ids0 not in f_map:
            f_map[ids0] = []
        if ids1 not in f_map:
            f_map[ids1] = []
        
        f_map[ids0].append(ids1)
        f_map[ids1].append(ids0)

    for emp_id,emp in emp_map.items():
        if emp not in result:
            result[emp] = []
        if emp_id in f_map:
            for fids in f_map[emp_id]:
                result[emp].append(emp_map[fids])
        else:
            result[emp] = None

    
    return result


# --- Runnable Example ---
employees = [
    "1, Bill, Engineer",
    "2, Joe, HR",
    "3, Sally, Engineer",
    "4, Richard, Business",
    "6, Tom, Engineer"
]

friendships = [
    "1, 2",
    "1, 3",
    "3, 4"
]

res = find_adjacencies(employees, friendships)
for name in res:
    print(name, ":", res[name])
# Expected:
#   Bill : Joe, Sally
#   Joe : Bill
#   Sally : Bill, Richard
#   Richard : Sally
#   Tom : None

"""
    Complexity Analysis:
    
    * Time Complexity: O(E + F)
      - E is the number of employees.
      - F is the number of friendships.
      - Building name map O(E), adjacency O(F), formatting O(E + F).
    
    * Space Complexity: O(E + F)
      - Name dictionary stores E entries.
      - Adjacency dictionary stores up to 2*F edges across all lists.
"""