def max_o_between(arr):
    """
    # For each ' ', treat it as 'x' and find the max count of 'o' 
    # between it and the nearest actual 'x' on both sides.
    # Return the index and max count that gives the best result.
    """
    index,max_count = 0, 0

    for i in range(len(arr)):

        if arr[i] == ' ': 
            # print(i)
            left_count,right_count,curr_count = 0,0,0
            j, k = i-1, i+1
            valid_left, valid_right = False, False
            while j>=0 :
                if arr[j] == 'o':
                    left_count+=1
                elif arr[j] == 'x':
                    valid_left = True
                    break
                else:
                    break
                j-=1
            while k<len(arr) :
                if arr[k] == 'o':
                    right_count+=1
                elif arr[k] == 'x':
                    valid_right = True
                    break
                else:
                    break
                k+=1
            

            if  valid_left and left_count > right_count:
                curr_count = left_count
            if valid_right and left_count < right_count:
                curr_count = right_count
            # print(i)
            if curr_count > max_count:
                max_count = curr_count
                # print(i)
                index = i 

    return (index,max_count)


# --- Runnable Example ---
arr1 = ['x', 'o', 'o', ' ', 'o', 'x', ' ', 'o', 'o', 'o', 'x']
print(max_o_between(arr1))
# Walkthrough:
#   i=3 (' '): left='o','o','x' -> left_count=2, right='o','x' -> right_count=1 -> max=2
#   i=6 (' '): left='x' -> left_count=0, right='o','o','o','x' -> right_count=3 -> max=3
# Expected: (6, 3)

arr2 = ['x', 'o', ' ', 'o', 'o', 'o', 'x']
print(max_o_between(arr2))
# i=2: left='o','x' -> 1, right='o','o','o','x' -> 3 -> max=3
# Expected: (2, 3)

arr3 = [' ', 'o', 'x']
print(max_o_between(arr3))
# i=0: no left, right='o','x' -> 1 -> max=1
# Expected: (0, 1)

"""
    Complexity Analysis:
    
    * Time Complexity: O(N^2)
      - For each ' ' (up to N), we scan left and right (up to N).
    
    * Space Complexity: O(1)
      - Only tracking counters and indices, no extra structures needed.
"""