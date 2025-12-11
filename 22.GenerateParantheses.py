#Pattern: Depth-First Search (DFS) using Stack
#Why this pattern?: We need to explore all possible combinations of parentheses.
#  Using a stack allows us to simulate the recursive process iteratively.
#Time Complexity: O(4^n / sqrt(n)) - This is the nth Catalan number, which represents the
#  number of valid parentheses combinations.
#Space Complexity: O(4^n / sqrt(n)) - This is the space needed to store all valid combinations.
class Solution:
    def generateParenthesis(self, n: int):
        # This list will store all valid combinations of parentheses
        result = []
        
        # Use a stack to simulate recursion.
        # Each element in the stack is a tuple:
        # (current_string, number_of_open_used, number_of_close_used)
        stack = [("", 0, 0)]
        
        # Process until all possible states are explored
        while stack:
            current, open_count, close_count = stack.pop()
            
            # If the current string has reached the full length (2*n),
            # then it's a valid complete parentheses combination.
            if len(current) == 2 * n:
                result.append(current)
                continue
            
            # Option 1: Add an opening parenthesis "("
            # Only allowed if we haven't used all n opening brackets yet.
            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))
            
            # Option 2: Add a closing parenthesis ")"
            # Only allowed if it will not create an invalid sequence.
            # That means: close_count < open_count
            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))
        
        # Return all valid combinations
        return result

sol = Solution()
print(sol.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
