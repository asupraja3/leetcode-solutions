def find_longest_song_sequence(songs, initial_song):
    """
    # Given a list of songs and an initial song, find the longest sequence where
    # each next song starts with the same word as the last word of the previous song.
    # Songs cannot repeat in the sequence.
    """
    result = []
    
    # 1. Build the dictionary connecting first words to songs
    word_connec = {}
    for song in songs:
        first = song.split()[0]
        if first not in word_connec:
            word_connec[first] = []
        word_connec[first].append(song)
    
    # 2. Initialize stack: (word_to_search, current_sequence)
    # Using .split()[-1] directly instead of a helper function
    to_check = [(initial_song.split()[-1], [])]
    
    # 3. Process the stack
    while to_check:
        last, current_path = to_check.pop()
        
        # Update our final result if this current path is the longest we've seen
        if len(current_path) > len(result):
            result = current_path

        if last in word_connec:
            for next_song in word_connec[last]:
                # Ensure we don't repeat a song in the current sequence
                if next_song not in current_path:
                    
                    # Get the new last word
                    next_last = next_song.split()[-1]
                    
                    # Create the new path and add it to the stack in a single line
                    to_check.append((next_last, current_path + [next_song]))

    return result
        

# --- Runnable Example ---
songs = [
    "hello world",
    "world of music",
    "music is life",
    "life goes on",
    "world class act",
    "act of kindness"
]
initial_song = "say hello"

print(find_longest_song_sequence(songs, initial_song))
# Expected: ["hello world", "world of music", "music is life", "life goes on"]
# Explanation:
#   "say hello" -> last word is "hello"
#   "hello world" -> last word is "world"
#   "world of music" -> last word is "music"
#   "music is life" -> last word is "life"
#   "life goes on" -> no song starts with "on", so sequence ends

"""
    Complexity Analysis:
    
    * Time Complexity: O(N! * W) in the worst case
      - N is the number of songs. In the worst case every song connects to every other,
        so we explore all possible orderings (permutations).
      - W is the average number of words per song (for splitting).
      - In practice, far fewer paths exist because not every song connects to every other.
    
    * Space Complexity: O(N * P)
      - N is the number of songs stored in our dictionary.
      - P is the number of paths we hold in to_check at any point.
      - Each path stores a copy of the visited set and the current sequence.
"""