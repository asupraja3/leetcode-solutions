"""
QUESTION: TRIPLET ANALYSIS

- You are given a string 'text'.
- Goal:
  Identify and count all triplets (three consecutive characters)
  where the FIRST and THIRD characters are the same.

- Rules:
  1. Comparison must be CASE-INSENSITIVE ('A' == 'a').
  2. Overlapping triplets are allowed and must be counted.
  3. Only consecutive triplets of length exactly 3 are considered.

- Examples:
  * "abA"   → 1 triplet ("abA")
  * "aaaa"  → 2 triplets ("aaa" at index 0, "aaa" at index 1)
"""

#Pattern: String Analysis & Triplet Counting
#Time Complexity: O(n) where n is the length of the input string
#Space Complexity: O(1) as we use a constant amount of extra space

def solution(text):
    n = len(text)

    # If the string has fewer than 3 characters,
    # no valid triplet can exist
    if n < 3:
        return 0

    triplet_count = 0

    # Iterate until the third-to-last character
    # so that i, i+1, and i+2 always form a valid triplet
    for i in range(n - 2):

        # Convert characters to lowercase for case-insensitive comparison
        first_char = text[i].lower()
        third_char = text[i + 2].lower()

        # Check if first and third characters match
        if first_char == third_char:
            triplet_count += 1

    return triplet_count


# Example Usage:
# text = "abcXccc"
# print(solution(text))
# Output: 2
#
# Explanation:
# Triplet 1: "abc" → 'a' != 'c'
# Triplet 2: "bcX" → 'b' != 'x'
# Triplet 3: "cXc" → 'c' == 'c' ✓
# Triplet 4: "Xcc" → 'x' != 'c'
# Triplet 5: "ccc" → 'c' == 'c' ✓
