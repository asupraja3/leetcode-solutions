def dept_cross_friends(employees, friendships):
    """
    # For each department, count employees who have at least one
    # friend in a different department.
    """

    empid_map = {}
    empdept_map = {}
    dept_totals = {}

    for val in employees:
        part = val.split(",")
        part1,part2,part3 = int(part[0].strip()),part[1].strip(),part[2].strip()
        empid_map[part1] = part2
        empdept_map[part2] = part3
        if part3 not in dept_totals:
            dept_totals[part3] = 0
        dept_totals[part3] += 1    
    frnd_map = {}
    result = {}
    for val in friendships:
        part = val.split(",")
        part1,part2= int(part[0].strip()),int(part[1].strip())
        if part1 not in frnd_map:
            frnd_map[part1] = []
        if part2 not in frnd_map:
            frnd_map[part2] = []
        
        frnd_map[part1].append(part2)
        frnd_map[part2].append(part1)
    
    print(empid_map,empdept_map,frnd_map)


    for id,emp in empid_map.items():
        
        empdept = empdept_map[emp]
        
        if empdept not in result:
            result[empdept] = 0

        if id not in frnd_map: #BUG_FIX: if no friends, then skip to next employee
            continue
        for fid in frnd_map[id]:
            if empdept != empdept_map[empid_map[fid]]:
                result[empdept]+=1
                break
        
    result2 = {}
    for dep,res in result.items():
        result2[dep] = str(res) + " of " +  str(dept_totals[dep])

    return result2


# --- Runnable Example ---
employees = [
    "1, Bill, Engineer",
    "2, Joe, HR",
    "3, Sally, Engineer",
    "4, Richard, Business",
    "6, Tom, Engineer"
]

friendships2 = [
    "1, 2",
    "1, 3",
    "3, 4",
    "6, 1"
]

res = dept_cross_friends(employees, friendships2)
for dept in res:
    print(dept, ":", res[dept])
# Expected:
#   Engineer: 2 of 3
#   HR: 1 of 1
#   Business: 1 of 1

