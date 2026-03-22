def is_valid_sudoku_variant(matrix):
    """
    # Valid Sudoku Variant: Given an n x n matrix, verify if every row 
    # and every column contains all numbers from 1 to n exactly once.
    """
    n = len(matrix)
    
    # Create the perfect set of expected numbers: {1, 2, ..., n}
    expected_numbers = set(range(1, n + 1))

    # Check every row
    for r in range(n):
        if set(matrix[r]) != expected_numbers:
            return False

    # Check every column
    for c in range(n):
        # Build a temporary list of the current column
        column = [matrix[r][c] for r in range(n)]
        
        if set(column) != expected_numbers:
            return False

    return True
        

# Example Usage
print(is_valid_sudoku_variant([
    [1, 2, 3], 
    [3, 1, 2], 
    [2, 3, 1]
])) 
# Expected output: True

"""
    Complexity Analysis:
    
    * Time Complexity: O(N^2)
      - N is the number of rows/columns. We look at every item in the N x N grid to check the rows, and then look at them all again to check the columns.
      
    * Space Complexity: O(N)
      - We store the `expected_numbers` set and a temporary `column` list, both of which only take up N space.
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

# ---------------------------------------------------------------------------------------------------

def word_search(board, word):
    """
    # Word Search: Determine if a specific word exists in a character grid, 
    # moving only horizontally or vertically.
    """

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    directions = [(-1,0),(0,-1),(1,0),(0,1)]

    i=0
    for r in range(rows):
        for c in range(cols):
            
            
            # If current cell matches the first character of the word, start a search from here
            if board[r][c] == word[0]:

                # Reset visited grid for each new starting cell
                visited = [[False for _ in range(cols)] for _ in range(rows)]

                # Stack holds (row, col, index into word) — each entry tracks its own position in the word
                to_check = [(r, c, 0)]

                # Mark starting cell as visited
                visited[r][c] = True

                while len(to_check) > 0:

                    # Pop the most recent cell and its corresponding word index
                    cur_r, cur_c, i = to_check.pop()

                    # If we've matched the last character, the full word has been found
                    if i == len(word) - 1:
                        return True

                    # Explore all 4 adjacent cells (up, left, down, right)
                    for (r1, c1) in directions:
                        next_row = r1 + cur_r
                        next_col = c1 + cur_c

                        # Check: in bounds, matches the next character in word, and not already visited
                        if (0 <= next_row < rows and 0 <= next_col < cols
                                and board[next_row][next_col] == word[i + 1]
                                and not visited[next_row][next_col]):

                            # Push neighbor onto stack with incremented word index
                            to_check.append((next_row, next_col, i + 1))

                            # Mark as visited to prevent reuse in this search
                            visited[next_row][next_col] = True                   

    return False

# Example Usage
grid = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(grid)
print(word_search(grid, "ABCCED")) 
# Expected output: True

print(word_search(grid, "ABCB")) 
# Expected output: False (You can't reuse the 'B')

"""
    Complexity Analysis:
    
    * Time Complexity: O(R * C * 4^L)
      - R is rows, C is columns, and L is the length of the word. In the worst case, we start a search at every cell, and from each cell, we explore 4 directions up to the length of the word.
      
    * Space Complexity: O(L)
      - The only extra memory used is the recursion stack, which goes as deep as the length of the word (L). Modifying the board in-place saves us from needing a separate visited matrix.
"""

# ---------------------------------------------------------------------------------------------------