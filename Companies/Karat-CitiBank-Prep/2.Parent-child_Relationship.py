def find_zero_and_one_parents(parent_child_pairs):
    """
    # Part 1: Given a list of parent-child pairs, return two lists: 
    # one for individuals with zero parents and one for individuals with exactly one parent.
    """
    parent_counts = {}

    # Step 1: Count parents for everyone
    for parent, child in parent_child_pairs:
        # Make sure both individuals are in our dictionary
        if parent not in parent_counts:
            parent_counts[parent] = 0
        if child not in parent_counts:
            parent_counts[child] = 0
            
        # The child gets one more parent
        parent_counts[child] += 1

    # Step 2: Sort them into lists based on their counts
    zero_parents = []
    one_parent = []
    
    for individual, count in parent_counts.items():
        if count == 0:
            zero_parents.append(individual)
        elif count == 1:
            one_parent.append(individual)

    return [zero_parents, one_parent]

# Input data: [Parent, Child]
pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), 
    (5, 7), (4, 5), (4, 8), (8, 9)
]

# Calling the function
result = find_zero_and_one_parents(pairs)
print(result)
# Expected Output: ([1, 2, 4], [5, 7, 8, 9])

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the number of pairs. We loop through the pairs exactly once.
      
    * Space Complexity: O(V)
      - V is the number of unique individuals. Our dictionary stores one entry per person.
"""

""" 
    Edge Cases to Consider:
    1. An empty list of pairs (should return two empty lists).
    2. All individuals have parents (zero parents list should be empty).
    3. All individuals have more than one parent (one parent list should be empty).
    4. A node has no ancestors (should return -1).
    5. Multiple nodes have the same earliest ancestor (should return any one of them).
    6. A non-tree structure (should handle gracefully, but we assume input is well-formed).
"""

# ---------------------------------------------------------------------------------------------------

def has_common_ancestor(parent_child_pairs, node1, node2):
    """
    # Part 2: Given two individuals, determine if they share at least one common ancestor.
    """
    # 1. Build a dictionary where a child points to a list of their parents
    parents_of = {}
    for parent, child in parent_child_pairs:
        if child not in parents_of:
            parents_of[child] = []
        parents_of[child].append(parent)

    # 2. Helper function to find all ancestors using a simple to-do list
    def get_all_ancestors(start_node):
        ancestors = set()
        to_check = [start_node]
        
        while len(to_check) > 0:
            curr = to_check.pop()
            
            # If this person has parents listed in our dictionary
            if curr in parents_of:
                for parent in parents_of[curr]:
                    if parent not in ancestors:
                        ancestors.add(parent)
                        to_check.append(parent) # Add parent to the to-do list to find THEIR parents
        return ancestors

    # 3. Get all ancestors for both people
    ancestors1 = get_all_ancestors(node1)
    ancestors2 = get_all_ancestors(node2)

    # 4. Check if they have anyone in common
    for ancestor in ancestors1:
        if ancestor in ancestors2:
            return True
            
    return False

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), 
    (5, 7), (4, 5), (4, 8), (8, 9) ]


print(has_common_ancestor(pairs, 5, 8)) # Expected: True (common ancestor is 4)

"""
    Complexity Analysis:
    
    * Time Complexity: O(V + E)
      - V is the number of unique individuals, E is the number of relationships (pairs). 
      - Building the graph takes O(E). Finding ancestors takes O(V + E) because we trace through the connections.
      
    * Space Complexity: O(V + E)
      - We store the relationships in a dictionary, and we create sets to hold the found ancestors.
"""

def find_earliest_ancestor(parent_child_pairs, node):
    """
    # Part 3: Find the "earliest ancestor" (the one furthest back in the tree) for a given person.
    """
    # 1. Build the same upward-pointing dictionary
    parents_of = {}
    for parent, child in parent_child_pairs:
        if child not in parents_of:
            parents_of[child] = []
        parents_of[child].append(parent)

    earliest_ancestor = -1
    max_distance = -1
    
    # 2. To-do list stores both the person AND how many generations back they are: (person, distance)
    to_check = [(node, 0)]
    visited = set()

    while len(to_check) > 0:
        curr, distance = to_check.pop()
        
        # 3. If we found someone further back, update our records
        # We also make sure the ancestor isn't the starting person themselves
        if distance > max_distance and curr != node:
            max_distance = distance
            earliest_ancestor = curr
            
        visited.add(curr)
        
        # 4. Add their parents to the to-do list, increasing the distance by 1
        if curr in parents_of:
            for parent in parents_of[curr]:
                if parent not in visited:
                    to_check.append((parent, distance + 1))
                    
    # Return the ancestor, or None if they had no parents
    return earliest_ancestor if earliest_ancestor != -1 else None

pairs = [
    (1, 3), (2, 3), (3, 6),
    (5, 6), (5, 7), (1, 5), 
    (4, 8), (8, 9) ]
print(find_earliest_ancestor(pairs, 6)) # Expected: 1 or 2 (both are equally far back)

"""
    Complexity Analysis:
    
    * Time Complexity: O(V + E)
      - We process each individual and their connections once as we travel up the tree.
      
    * Space Complexity: O(V + E)
      - We store the relationships in the `parents_of` dictionary, and the `visited` set tracks the individuals.
"""