def find_first_word(s, words):
    """
    # Given a string and array of words, find the first word that can be
    # constructed using letters from the string (each letter used at most
    # as many times as it appears in the string).
    """
    # 1. Build frequency map of the string
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    # 2. Check each word
    for word in words:
        # Build frequency map for current word
        word_freq = {}
        for ch in word:
            if ch not in word_freq:
                word_freq[ch] = 0
            word_freq[ch] += 1
        
        # 3. Check if every char in word is available in string
        valid = True
        for ch in word_freq:
            if ch not in freq or word_freq[ch] > freq[ch]:
                valid = False
                break
        
        if valid:
            return word
    
    # 4. No word can be formed
    return None


# --- Runnable Example ---
print(find_first_word("balloons", ["son", "ball", "friends"]))
# Expected: "son"
# Walkthrough:
#   freq of "balloons": {b:1, a:1, l:2, o:2, n:1, s:1}
#   "son" -> {s:1, o:1, n:1} -> all available -> return "son"

print(find_first_word("balloons", ["sond", "friends", "son", "ball"]))
# Expected: "son"
# "sond" -> needs d, not available
# "friends" -> needs f, not available
# "son" -> all available -> return "son"

print(find_first_word("abc", ["dd", "ee", "ff"]))
# Expected: None

print(find_first_word("aabb", ["aab", "bba", "aaab"]))
# Expected: "aab"
# "aab" -> needs a:2, b:1 -> available -> return "aab"

"""
    Complexity Analysis:
    
    * Time Complexity: O(S + W * L)
      - S is the length of the string (to build freq map).
      - W is the number of words, L is the avg length of each word.
      - For each word we build its freq map and compare.
    
    * Space Complexity: O(S + L)
      - freq map for string and word_freq for current word.
"""