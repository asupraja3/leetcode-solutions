def word_search(board, word):
    """
    # Find the word in the matrix moving only right and down.
    # Return the list of (row, col) positions where each letter was found.
    # Word is guaranteed to exist in the matrix.
    """

    directions = [(0,1),(1,0)]

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    # result = []

    for i in range(rows):
        for j in range(cols):

            if board[i][j] == word[0]:
                to_check = [(i,j,[(i,j)],0)]
                # k=0
                while len(to_check) > 0:
                    curr_i , curr_j,curr_path,k = to_check.pop()
                    if k == len(word) - 1:
                        return curr_path

                    for move_i, move_j in directions:

                        next_i = move_i + curr_i
                        next_j = move_j + curr_j

                        if k<len(word)-1 and 0<=next_i<rows and 0<=next_j<cols and board[next_i][next_j] == word[k+1]:
                            to_check.append((next_i,next_j,curr_path+[(next_i,next_j)],k+1))
                            # k+=1

    return []


# --- Runnable Example ---
board1 = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(word_search(board1, "BCCE"))
# Expected: [(0,1), (0,2), (1,2), (2,2)]
# Walkthrough:
#   B(0,1) -> right C(0,2) -> down C(1,2) -> down E(2,2)

board2 = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
print(word_search(board2, "BEF"))
# Expected: [(0,1), (1,1), (1,2)]
# Walkthrough:
#   B(0,1) -> down E(1,1) -> right F(1,2)

board3 = [
    ['A', 'B'],
    ['C', 'D']
]
print(word_search(board3, "ABD"))
# Expected: [(0,0), (0,1), (1,1)]
# Walkthrough:
#   A(0,0) -> right B(0,1) -> down D(1,1)

"""
    Complexity Analysis:
    
    * Time Complexity: O(R * C * 2^L)
      - R*C to try each starting cell.
      - At each step we branch into 2 directions (right, down).
      - L is the length of the word, so max 2^L paths per start.
    
    * Space Complexity: O(L)
      - to_check list and path store at most L items deep.
"""