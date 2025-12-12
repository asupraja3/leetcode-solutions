#Pattern : Backtracking
#Why this pattern?: We need to explore all possible combinations of letters for the given digits.
#Time Complexity: O(3^m * 4^n) where m is the number of digits that map to 3 letters
# and n is the number of digits that map to 4 letters. This is because each digit can
# lead to multiple branches in the recursion tree.
#Space Complexity: O(m + n) for the recursion stack, where m is the number of digits
# that map to 3 letters and n is the number of digits that map to 4 letters.

class Solution:
    def letterCombinations(self, digits):
        # If input is empty, there are no combinations to generate.
        if not digits:
            return []

        # Mapping from digit → possible letters (same as phone keypad).
        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = []  # This will store all the generated combinations

        # Backtracking function to build each possible combination
        def backtrack(index, current_combination):
            """
            index:     which digit we are currently processing
            current_combination: the letters built so far as a partial answer
            """

            # If the length of the current combination equals the length of digits,
            # it means we have formed a complete valid combination.
            if index == len(digits):
                result.append(current_combination)
                return

            # Get all possible letters for the current digit.
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            # Try each letter and continue building the combination.
            for letter in possible_letters:
                # Add the current letter to the partial combination
                # and move to the next digit (index + 1)
                backtrack(index + 1, current_combination + letter)

        # Start backtracking from index 0 with an empty combination
        backtrack(0, "")

        return result
Sol = Solution()
print(Sol.letterCombinations("23"))  # Expected output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]