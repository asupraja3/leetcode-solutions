def word_search_multiple(board, words):
    """
    # Find multiple words in the matrix moving only right and down.
    # Each cell can only be used by one word.
    # Return dict of word -> list of (row, col) positions.
    """
    result = {}

    if not words or not board:
        return result

    rows = len(board)
    cols = len(board[0])
    
    # Global set to track cells claimed by previously found words
    used_cells = set()
    directions = [(1, 0), (0, 1)] # Down, Right

    # 1. Loop through each word we want to find
    for word in words:
        if not word:
            continue
            
        word_found = False
        
        # 2. Scan the board for the first letter of the current word
        for i in range(rows):
            if word_found: break
            
            for j in range(cols):
                if word_found: break
                
                # 3. Start search if letter matches and cell is not claimed
                if board[i][j] == word[0] and (i, j) not in used_cells:
                    to_check = [(i, j, [(i, j)], 0)]
                    
                    # 4. Process the DFS stack
                    while len(to_check) > 0:
                        curr_i, curr_j, curr_path, k = to_check.pop()

                        # Check if we found the whole word
                        if k == len(word) - 1:
                            result[word] = curr_path
                            # Claim these cells so next words can't use them
                            for r, c in curr_path:
                                used_cells.add((r, c))
                            word_found = True
                            break # Stop searching the stack for this word

                        # Look down and right for the next letter
                        for move_i, move_j in directions:
                            next_i = curr_i + move_i
                            next_j = curr_j + move_j
                            
                            # Ensure we are in bounds, letters match, and cell is free
                            if (0 <= next_i < rows and 
                                0 <= next_j < cols and 
                                k < len(word) - 1 and 
                                board[next_i][next_j] == word[k + 1] and 
                                (next_i, next_j) not in used_cells):
                                
                                to_check.append((next_i, next_j, curr_path + [(next_i, next_j)], k + 1))

    return result


# --- Runnable Example ---
board1 = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['D', 'E', 'E', 'E']
]
words1 = ["BCCE", "SDE"]

res = word_search_multiple(board1, words1)
for word in res:
    print(word, ":", res[word])
# Expected:
#   BCCE : [(0, 1), (0, 2), (1, 2), (2, 2)]
#   SDE  : [(1, 0), (2, 0), (2, 1)]

board2 = [
    ['A', 'B'],
    ['C', 'D']
]
words2 = ["AB", "CD"]

res2 = word_search_multiple(board2, words2)
for word in res2:
    print(word, ":", res2[word])
# Expected:
#   AB : [(0, 0), (0, 1)]
#   CD : [(1, 0), (1, 1)]

"""
    Complexity Analysis:
    
    * Time Complexity: O(W * R * C * 2^L)
      - W is the number of words.
      - R*C to try each starting cell per word.
      - 2^L paths per start where L is max word length.
    
    * Space Complexity: O(W * L + R * C)
      - Result stores paths for W words (W * L space).
      - Used set can hold up to R*C cells.
"""