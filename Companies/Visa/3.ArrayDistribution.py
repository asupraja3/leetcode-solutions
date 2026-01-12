"""
QUESTION: ARRAY DISTRIBUTION

- You are given an array 'numbers'.
- Goal:
  Distribute the elements into two arrays: 'first' and 'second'
  based on comparison rules.

- Initialization:
  * first  = [numbers[0]]
  * second = [numbers[1]]

- Distribution Rules for numbers[i] (i >= 2):
  1. Count how many elements in 'first' are strictly greater than numbers[i].
  2. Count how many elements in 'second' are strictly greater than numbers[i].
  3. Place numbers[i] in the array with the HIGHER count.
  4. If counts are tied, place it in the array with the SHORTER length.
  5. If lengths are also tied, place it in the 'first' array.
- Final Step:
  Append 'second' array to the end of 'first' and return the result.
"""

#Pattern: Array Distribution & Counting
#Time Complexity: O(n^2) due to nested counting loops for each element
#Space Complexity: O(n) for storing elements in two separate arrays, 
# where n is the number of elements in the input array.

def solution(numbers):
    n = len(numbers)

    # Edge cases
    if n == 0:
        return []
    if n == 1:
        return [numbers[0]]

    # Initial placement as per problem statement
    first = [numbers[0]]
    second = [numbers[1]]

    # Process elements starting from index 2
    for i in range(2, n):
        val = numbers[i]

        # Count elements strictly greater than val in 'first'
        count_first = sum(1 for x in first if x > val)

        # Count elements strictly greater than val in 'second'
        count_second = sum(1 for x in second if x > val)

        # Rule 3: Place in array with higher count
        if count_first > count_second:
            first.append(val)
        elif count_second > count_first:
            second.append(val)
        else:
            # Rule 4 & 5: Tie-breaking using array length
            if len(first) <= len(second):
                first.append(val)
            else:
                second.append(val)

    # Final concatenation
    return first + second


# Example Usage:
numbers = [5, 7, 6, 9, 2]
print(solution(numbers))
# Output: [5, 9, 2, 7, 6]
