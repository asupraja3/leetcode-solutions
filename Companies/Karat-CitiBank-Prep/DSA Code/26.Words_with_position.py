def find_words_with_positions(board, words):
    """
    # Find all words from the list in the board (moving right and down).
    # Return each word with the (row, col) positions where it was found.
    """

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    result = {}

    for word in words:
        # visited = [[False for _ in range(cols)] for _ in range(rows)]
        word_found = False
        for i in range(rows):
            if word_found: break
            for j in range(cols):
                if word_found: break
                if word not in result:
                    result[word] = []
                # result[word]
                if word[0] != board[i][j]:
                    continue
                to_check = [(i,j,0,[(i,j)])]
                # visited[i][j] = True
                while len(to_check) > 0:
                    curr_i, curr_j, k, curr_path = to_check.pop()
                    if k == len(word) - 1:
                        result[word] = curr_path
                        # word_found = True
                        break
                    for move_i,move_j in direction:
                        next_i,next_j = (curr_i + move_i), (curr_j + move_j)

                        if k<len(word) and 0<=next_i<rows and 0<=next_j < cols and board[next_i][next_j] == word[k+1]:
                            # and not visited[next_i][next_j]:

                            to_check.append((next_i,next_j,k+1,curr_path+[(next_i,next_j)]))
                            # visited[next_i][next_j] = True


    return result





# --- Runnable Example ---
grid = [
    ['c', 'c', 't', 'n', 'a', 'x'],
    ['c', 'c', 'a', 't', 'n', 't'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'n', 'i', 'i', 'p', 'p'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i'],
]

words = ["catnip", "cccc", "ant", "aoi", "ki", "aaoo", "ooo"]

res = find_words_with_positions(grid, words)
for word in res:
    print(word, ":", res[word])
# Expected (paths going right/down):
#   catnip : [(0,0), (1,0), (1,1), ...]  etc
#   cccc   : [(0,0), (0,1), (1,1), (2,1)]
#   ooo    : [(4,1), (4,2), (4,3)]
#   ...each word with its coordinate path