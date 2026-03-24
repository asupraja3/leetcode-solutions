def find_first_zero(matrix):
    """
    # Part 1: Given a 2D matrix of 0s and 1s, write a function 
    # to find the coordinates (row, col) of the first 0.
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                return (r, c) # Return immediately upon finding the first 0
                
    return None # Return None if no 0 is found

print(find_first_zero([[1, 1, 1], [1, 0, 1], [1, 1, 1]])) 
# Expected output: (1, 1)

"""
    Complexity Analysis:
    
    * Time Complexity: O(R * C)
      - R is the number of rows, C is the number of columns.
      - In the worst-case scenario (the 0 is in the very last cell, or there are no 0s at all), the nested loops must check every single cell once.
      
    * Space Complexity: O(1)
      - We are only storing a few basic variables for our coordinates and grid dimensions.
      - No additional data structures or matrices are created, meaning the memory used stays completely constant regardless of how massive the grid gets.
"""

""" 
    Edge Cases to Consider:
    1. An empty matrix (should return None).
    2. A matrix with no 0s (should return None).
    3. A matrix where the first cell (0, 0) is a 0 (should return (0, 0)).
    4. A matrix where the last cell is a 0 (should return the coordinates of the last cell).
    5. A matrix with multiple 0s (should return the coordinates of the first one found).
    6. A non-rectangular matrix (should handle gracefully, but we assume input is well-formed).
"""
# -------------------------------------------------------------------------------------------------

def find_rectangles(matrix):  
    """
    # Part 2: Expand the code to find the top-left and bottom-right 
    # coordinates of all rectangular shapes composed of 0s in the grid.
    """

    rectangles = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0 and not visited[r][c]:

                curr_c = c
                while curr_c < cols and  matrix[r][curr_c] == 0:
                    curr_c+=1
                
                curr_r = r
                while curr_r < rows:
                    row_is_valid = True
                    for col_idx in range(c, curr_c):
                        if matrix[curr_r][col_idx] != 0:
                            row_is_valid = False
                            break
                    
                    if not row_is_valid:
                        break
                    curr_r += 1

                top_left = (r,c)
                bottom_right = (curr_r -1,curr_c-1)
                rectangles.append((top_left,bottom_right))

                for i in range(r,curr_r):
                    for j in range(c,curr_c):
                        visited[i][j] = True


    return rectangles


print(find_rectangles([[1, 0, 0, 1,1], 
                       [1, 0, 1, 1,1], 
                       [1, 1, 1, 1,1], 
                       [1, 0, 0, 1,1], 
                       [0, 0, 0, 0,0]])) 
# Expected output: [((0, 1), (1, 2)), ((3, 0), (3, 4))]

"""
    Complexity Analysis:
    
    * Time Complexity: O(R * C)
      - R is the number of rows, C is the number of columns.
      - We iterate through every cell in the matrix using the outer loops.
      - The `visited` matrix ensures that the inner loops only process and mark the cells of each rectangle exactly once, keeping the time strictly linear to the grid size.
      
    * Space Complexity: O(R * C)
      - The separate boolean `visited` matrix requires exactly R * C memory to map every cell.
      - In the worst-case scenario (a grid full of alternating 1x1 rectangles), the `rectangles` output list will also scale proportionally with the grid size.
"""

""" 
    Edge Cases to Consider:
    1. An empty matrix (should return an empty list).
    2. A matrix with no 0s (should return an empty list).
    3. A matrix where the entire grid is 0s (should return one rectangle covering the whole grid).
    4. A matrix with multiple distinct rectangles (should return the correct coordinates for each).
    5. A matrix with rectangles that touch each other (should still identify them as separate rectangles).
    6. A non-rectangular matrix (should handle gracefully, but we assume input is well-formed).
"""

# -------------------------------------------------------------------------------------------------

def find_shapes(matrix):
    """
    # Part 3: Modify the solution to handle non-rectangular shapes (islands of 0s) 
    # and return the list of all coordinates belonging to each distinct shape.
    """
    shapes = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # 1. Create your separate boolean visited matrix
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            
            # 2. When we find an unvisited 0, we have discovered a new shape
            if matrix[r][c] == 0 and not visited[r][c]:
                current_shape = []
                
                # 3. Create a simple "to-do list" to track connected 0s
                to_check = [(r, c)]
                visited[r][c] = True # Mark it immediately so we don't check it twice
                
                # 4. Keep working through the to-do list until it's empty
                while len(to_check) > 0:
                    curr_r, curr_c = to_check.pop()
                    current_shape.append((curr_r, curr_c))
                    
                    #Why -1?: Shapes are not always simple blocks: While the outer loop moves top-to-bottom,
                    # a single shape can be complex, like a "U" shape or a "C" shape.
                    # Look Up, Down, Left, and Right
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for move_r, move_c in directions:
                        next_r = curr_r + move_r
                        next_c = curr_c + move_c
                        
                        # 5. If the neighbor is inside the grid, is a 0, and is unvisited
                        if (0 <= next_r < rows and 0 <= next_c < cols and 
                            matrix[next_r][next_c] == 0 and not visited[next_r][next_c]):
                            
                            visited[next_r][next_c] = True
                            
                            # Add this neighbor to the to-do list so we can check ITS neighbors later
                            to_check.append((next_r, next_c)) 
                            
                # 6. Once the to-do list is empty, the entire shape has been found
                shapes.append(current_shape)
                
    return shapes


# A grid containing exactly two distinct shapes of 0s
sample_matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1], # <-- Shape 1 starts here
    [1, 0, 0, 0, 1], # <-- Shape 1 ends here
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1], # <-- Shape 2 starts here
    [1, 1, 1, 0, 1]  # <-- Shape 2 ends here
]

# Call the function we just wrote
result = find_shapes(sample_matrix)

# Print the final list of shapes
print(result)

"""
    Complexity Analysis:
    
    * Time Complexity: O(R * C)
      - R is the number of rows, C is the number of columns.
      - We loop through every cell in the grid. 
      - The `visited` matrix ensures we never process the same cell twice in our 'to-do list'.
      
    * Space Complexity: O(R * C)
      - The `visited` matrix requires exactly R * C space.
      - In the worst-case scenario (a grid completely full of 0s), the 'to-do list' 
        and the final 'shapes' list will also grow to hold every coordinate.
"""


# -------------------------------------------------------------------------------------------------

def is_valid_matrix(matrix):
    """
    # Alternative: Determine if every row and column in a square matrix 
    # contains all numbers from 1 to n (like a Sudoku validator).
    """
    n = len(matrix)
    
    # 1. Create a "perfect" set of numbers we expect to see. 
    # For a 3x3 matrix, this creates {1, 2, 3}
    expected_numbers = set(range(1, n + 1))

    # 2. Check every row
    for r in range(n):
        # Convert the current row to a set. 
        # If it has duplicates or wrong numbers, it won't match 'expected_numbers'
        if set(matrix[r]) != expected_numbers:
            return False

    # 3. Check every column
    for c in range(n):
        # Build the column by grabbing the c-th item from every row
        column = [matrix[r][c] for r in range(n)]
        
        # Check the column exactly like we checked the row
        if set(column) != expected_numbers:
            return False

    # 4. If we checked every row and column without failing, it is valid
    return True

print(is_valid_matrix([
    [1, 2, 3], 
    [3, 1, 2], 
    [2, 3, 1]
])) 
# Expected output: True

print(is_valid_matrix([
    [1, 2, 3], 
    [3, 1, 2], 
    [2, 2, 2]
])) 
# Expected output: False


"""
    Complexity Analysis:
    
    * Time Complexity: O(N^2)
      - N is the number of rows (and columns, since it is a square matrix).
      - We iterate through the matrix twice: once row-by-row, and once column-by-column. 
      - Checking every single item out of the total N * N items gives us a quadratic time complexity.
      
    * Space Complexity: O(N)
      - We create the `expected_numbers` set, which takes N space.
      - During the column check, we create a temporary `column` list that also takes N space.
      - We do not recreate the entire N x N grid, keeping our memory usage strictly
        proportional to a single row or column.
"""