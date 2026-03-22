def find_song_pair(song_times):
    """
    # Given a list of songs with durations, find two distinct songs
    # that add up to exactly 7 minutes (420 seconds).
    """
    # 1. Helper function to cleanly convert time strings to seconds
    def get_seconds(time_str):
        mins, secs = time_str.split(":")
        return int(mins) * 60 + int(secs)

    # 2. Dictionary to remember what time we need to complete a pair
    # Format: {needed_seconds: "Song Name"}
    needed_times = {}

    # 3. Loop through the songs exactly once
    for song, time_str in song_times:
        current_seconds = get_seconds(time_str)
        
        # If this song's time exactly matches what a previous song was looking for
        if current_seconds in needed_times:
            # We found a match! Return the previous song and the current song
            return [needed_times[current_seconds], song]
            
        # Otherwise, calculate what time this current song needs to hit 420
        needed_to_reach_420 = 420 - current_seconds
        
        # Store it in the dictionary for future songs to check against
        needed_times[needed_to_reach_420] = song

    # 4. Return an empty list if no pair is ever found
    return []


# --- Runnable Example ---
song_times_1 = [
    ("Stairway to Heaven", "8:05"),
    ("Immigrant Song", "2:27"),
    ("Rock and Roll", "3:41"),
    ("Communication Breakdown", "2:29"),
    ("Good Times Bad Times", "2:48"),
    ("Hot Dog", "3:19"),
    ("The Crunge", "3:18"),
    ("Achilles Last Stand", "10:26"),
    ("Black Dog", "4:55")
]

print(find_song_pair(song_times_1))
# Expected: ["Rock and Roll", "Hot Dog"]
# Explanation:
#   "Rock and Roll" = 3:41 = 221 seconds
#   "Hot Dog"       = 3:19 = 199 seconds
#   221 + 199 = 420 seconds = exactly 7 minutes

"""
    Complexity Analysis:
    
    * Time Complexity: O(N)
      - N is the number of songs.
      - Building the dictionary takes O(N). 
      - Checking each song for its complement takes O(N).
      - Dictionary lookup is O(1) on average.
    
    * Space Complexity: O(N)
      - We store all songs in a dictionary and in the to_check list.
"""