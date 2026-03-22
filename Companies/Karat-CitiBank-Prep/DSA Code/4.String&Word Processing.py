
def find_valid_words(words, available_chars):
    """
    # Part 1: Given a list of words and a string of available characters, 
    # identify which words from the list can be fully formed using only those characters.
    """

    # 1. Count our available characters
    char_bank = {}
    for char in available_chars:
        if char not in char_bank:
            char_bank[char] = 0
        char_bank[char] += 1

    valid_words = []

    # 2. Check each word
    for word in words:
        # Make a fresh copy of the bank for this specific word
        temp_bank = char_bank.copy()
        can_form = True

        for char in word:
            # If the character isn't in the bank, or we ran out of it
            if char not in temp_bank or temp_bank[char] == 0:
                can_form = False
                break
            # Otherwise, use one up
            temp_bank[char] -= 1

        if can_form:
            valid_words.append(word)

    return valid_words



print(find_valid_words(["cat", "dog", "tac", "god", "act"], "tcaog"))
# Expected output: ['cat', 'tac', 'act']



"""
    Complexity Analysis:
    
    * Time Complexity: O(C + W * L)
      - C is the number of available characters, W is the number of words, and L is the max length of a word.
      - We loop through the available characters once, and then check each letter of every word.
      
    * Space Complexity: O(C)
      - We store the counts of the available characters in our dictionary. The maximum size of this dictionary is the number of unique characters in the string (usually bounded by 26 for lowercase English letters).
"""

""" 
    Edge Cases to Consider:
    1. An empty list of words (should return an empty list).
    2. An empty string of available characters (should return an empty list).
    3. Words that require characters not in the available string (should not be included in the result).
    4. Words that require more instances of a character than are available (should not be included in the result).
    5. Words that can be formed exactly with the available characters (should be included in the result).
    6. Words that can be formed with a subset of the available characters (should be
         included in the result).
    7. A very large list of words or a long string of available characters (should still perform efficiently).
"""

# ---------------------------------------------------------------------------------------------------

def find_longest_valid_word(words, available_chars):
    """
    # Part 2: Find the longest word that can be formed from the list.
    """
    longest_word = None

    max_len = 0
    valid_words = find_valid_words(words, available_chars)

    for word in valid_words:
        if len(word) > max_len:
            longest_word = word
            max_len = len(word)

    return longest_word

print(find_longest_valid_word(["cat", "catch", "dog", "good"], "catcgho"))
# Expected output: 'catch'
"""
    Complexity Analysis:
    
    * Time Complexity: O(C + W * L)
      - We do the exact same work as Part 1, plus one extra pass over the valid words (which is at most W words).
      
    * Space Complexity: O(C + W)
      - We store the dictionary of characters O(C) and the temporary list of valid words O(W) before returning the longest one.
"""

# ---------------------------------------------------------------------------------------------------

def justify_text(words, max_width):
    """
    # Part 3 (Text Justification): Given a sequence of words and a line width, 
    # format the text so each line has the exact width, distributing spaces evenly.
    """
    result = []

    current_line = []
    current_length = 0
    for word in words:
        # Check if adding this word would exceed the max width (considering spaces)
        if current_length + len(word) + len(current_line) > max_width:
            # Time to justify the current line
            total_spaces = max_width - current_length
            if len(current_line) == 1:
                # If there's only one word, left-justify it
                result.append(current_line[0] + ' ' * total_spaces)
            else:
                # Distribute spaces evenly
                spaces_between_words = total_spaces // (len(current_line) - 1)
                extra_spaces = total_spaces % (len(current_line) - 1)

                line = ""
                for i in range(len(current_line) - 1):
                    line += current_line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
                line += current_line[-1]  # Add the last word without extra space
                result.append(line)

            # Start a new line with the current word
            current_line = [word]
            current_length = len(word)
        else:
            # Add the word to the current line
            current_line.append(word)
            current_length += len(word)
    # Handle the last line (left-justified)
    if current_line:
        line = ' '.join(current_line)
        line += ' ' * (max_width - len(line))  # Pad the end with spaces
        result.append(line)

    return result


# Example Usage
sample_words = ["This", "is", "an", "example", "of", "text", "justification."]
formatted_text = justify_text(sample_words, 16)

for line in formatted_text:
    print(f"'{line}'")
# Expected output:
# 'This    is    an'
# 'example  of text'
# 'justification.  '


"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the total number of characters across all words. We touch each word a constant number of times to add it to a line and distribute spaces.
      
    * Space Complexity: O(N)
      - We store the constructed strings in our `result` list and `current_line` list, which will ultimately hold all the characters and spaces.
"""