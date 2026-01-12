"""
QUESTION: BUILDING STRUCTURES (STEPWISE PATTERN)

- You are given an array 'structures' representing building heights.
- Goal:
  Transform the array into a "stepwise" pattern where the height difference
  between adjacent buildings is exactly 1.

- Valid patterns:
  1. Ascending  → [H, H+1, H+2, ...]
  2. Descending → [H, H-1, H-2, ...]

- Constraint:
  You are ONLY allowed to increase building heights.
  You cannot decrease any value.

- Output:
  Return the minimum total height units added to form
  either ascending or descending pattern.
"""

#Pattern: Greedy with Mathematical Offset
# Time Complexity: O(n), where n is the number of buildings 
# Space Complexity: O(1)

def solution(structures):
    n = len(structures)

    # If there are 0 or 1 buildings, no additions are needed
    if n <= 1:
        return 0

    def calculate_min_additions(heights, mode="ascending"):
        """
        Calculates the minimum height additions required
        to form a valid stepwise pattern.

        mode = "ascending"  → increasing by 1 each step
        mode = "descending" → decreasing by 1 each step
        """

        # Let H be the height of the first building in the pattern.
        #
        # Ascending pattern:
        #   final_height[i] = H + i
        #   Constraint: H + i >= heights[i]
        #   => H >= heights[i] - i
        #
        # Descending pattern:
        #   final_height[i] = H - i
        #   Constraint: H - i >= heights[i]
        #   => H >= heights[i] + i

        if mode == "ascending":
            # Minimum possible starting height H
            base_H = max(heights[i] - i for i in range(n))

            # Total units added = sum of (final_height - original_height)
            total_added = sum(
                (base_H + i) - heights[i] for i in range(n)
            )

        else:  # descending
            # Minimum possible starting height H
            base_H = max(heights[i] + i for i in range(n))

            # Total units added = sum of (final_height - original_height)
            total_added = sum(
                (base_H - i) - heights[i] for i in range(n)
            )

        return total_added

    # Compute cost for both patterns
    cost_ascending = calculate_min_additions(structures, "ascending")
    cost_descending = calculate_min_additions(structures, "descending")

    # Return the minimum cost
    return min(cost_ascending, cost_descending)


# Example Usage:
structures = [1, 4, 3, 2]
print(solution(structures))
# Output: 4
# Explanation: Best pattern is [5, 4, 3, 2]
