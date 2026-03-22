import copy
def check_sprinkler_coverage(grid, sprinklers):
    """
    # Given a 2D grid and list of sprinklers with positions and strength,
    # check if all required cells (marked '.' or 'dry') are covered.
    # A sprinkler at (r,c) with strength s covers a square from
    # (r-s, c-s) to (r+s, c+s).
    """

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    # result = {}
    # grid2 = copy.deepcopy(grid)
    # grid2 = grid.copy() # shallow copy is enough since we will overwrite entire rows
    grid2 = [row.copy() for row in grid] # deep copy of 2D list
    for sprink in sprinklers:
        # direction = [(0,sprink[2]), (sprink[2],0), (0,-sprink[2]), (sprink[2],0)]
        i1= sprink[0]- sprink[2] if sprink[0] - sprink[2] > 0 else 0
        j1 = sprink[1]- sprink[2] if sprink[1] - sprink[2] > 0 else 0
        i2 = sprink[0] + sprink[2] if sprink[0] + sprink[2] < rows else rows-1
        j2 = sprink[1]+ sprink[2] if sprink[1] + sprink[2] < cols else cols-1

        # c_start = max(0, c - s)
        # c_end = min(cols - 1, c + s)

        for i in range(i1,i2+1):
            for j in range(j1, j2+1):
                grid2[i][j] = 'X'
        # for i in range(rows):
        #     for j in range(cols):
    no_X = []
    covered = True
    for i in range(rows):
        for j in range(cols):
            if grid2[i][j] != 'X':
                no_X.append((i,j))
                covered = False


    # print(grid)      

    return (covered,no_X)




# --- Runnable Example ---
grid1 = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
]

# Sprinkler at (1,1) strength 1, and (3,3) strength 1

sprinklers1 = [(1, 1, 1), (3, 3, 1)]
all_covered, missed = check_sprinkler_coverage(grid1, sprinklers1)
print("All covered:", all_covered)
print("Missed cells:", missed)

# Walkthrough:
#   Sprinkler (1,1,1): covers (0,0) to (2,2)
#   Sprinkler (3,3,1): covers (2,2) to (4,4)
#   Missed: (0,3), (0,4), (1,3), (1,4) etc — right side uncovered
# Expected: False, [(0,3), (0,4), (1,3), (1,4)]

# Full coverage example
sprinklers2 = [(2, 2, 1)]
all_covered2, missed2 = check_sprinkler_coverage(grid1, sprinklers2)
print("\nAll covered:", all_covered2)
print("Missed cells:", missed2)
# Sprinkler (2,2,1): covers entire 5x5 grid
# Expected: True, []

# Edge case: sprinkler at corner
grid2 = [
    ['.', '.'],
    ['.', '.'],
]
sprinklers3 = [(0, 0, 1)]
all_covered3, missed3 = check_sprinkler_coverage(grid2, sprinklers3)
print("\nAll covered:", all_covered3)
print("Missed cells:", missed3)
# Sprinkler (0,0,1): covers (0,0) to (1,1) — clamped at boundaries
# Expected: True, []