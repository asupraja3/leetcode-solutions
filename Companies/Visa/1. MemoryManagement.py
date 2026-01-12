"""
QUESTION: MEMORY MANAGEMENT (ALLOC/ERASE)

- You manage a memory array consisting of:
  0 -> free memory unit
  1 -> occupied memory unit

- Alignment Rule:
  Every allocation must start at an index divisible by 8 (0, 8, 16, ...).

- Alloc(x):
  Find the first aligned index where x consecutive units are free.
  If found:
    - Mark those units as occupied (1)
    - Assign a unique ID (starting from 1)
    - Return the starting index
  If not found:
    - Return -1

- Erase(ID):
  If the given ID exists:
    - Free all its units (set to 0)
    - Return the length of the freed block
  If ID does not exist:
    - Return -1
"""

#Pattern: Memory Management & HashMap & Simulation
#Time Complexity: O(M * N), where M is the number of queries and N is
# the length of the memory array in the worst case for each allocation.
#Space Complexity: O(K), where K is the number of currently allocated blocks.
# Explained: We use a dictionary to track allocated blocks by their IDs.

class MemoryManager:
    def __init__(self, initial_memory):
        # Copy the input memory array so original data is not modified
        self.memory = list(initial_memory)
        
        # Counter to generate unique IDs for each allocation
        self.id_counter = 1
        
        # Dictionary to track allocated blocks
        # Key   -> allocation ID
        # Value -> (start_index, block_length)
        self.allocated_blocks = {}

    def alloc(self, x):
        """
        Allocate x consecutive memory units.
        Returns the starting index if successful, otherwise -1.
        """
        n = len(self.memory)

        # Only check indices divisible by 8 to satisfy alignment rule
        for start in range(0, n, 8):
            
            # Ensure x units fit within memory bounds
            if start + x <= n:
                
                # Check if all x units are free (value == 0)
                if all(self.memory[i] == 0 for i in range(start, start + x)):
                    
                    # Mark the memory units as occupied
                    for i in range(start, start + x):
                        self.memory[i] = 1
                    
                    # Save allocation metadata using current ID
                    self.allocated_blocks[self.id_counter] = (start, x)
                    
                    # Increment ID for next allocation
                    self.id_counter += 1
                    
                    # Return starting index of allocated block
                    return start

        # No valid aligned free block found
        return -1

    def erase(self, block_id):
        """
        Free the memory block associated with block_id.
        Returns the length of the freed block, or -1 if ID not found.
        """
        # Check if the block ID exists
        if block_id in self.allocated_blocks:
            
            # Retrieve start index and length
            start, length = self.allocated_blocks[block_id]
            
            # Free the memory units by setting them back to 0
            for i in range(start, start + length):
                self.memory[i] = 0
            
            # Remove block information from tracking
            del self.allocated_blocks[block_id]
            
            # Return the size of the freed block
            return length

        # Invalid block ID
        return -1


def solution(memory, queries):
    """
    Processes a list of allocation and erase queries.

    memory  -> initial memory state (list of 0s and 1s)
    queries -> list of [type, value]
               type 0 = alloc(value)
               type 1 = erase(value)
    """
    manager = MemoryManager(memory)
    results = []

    # Process each query in order
    for q_type, val in queries:
        if q_type == 0:        # Allocation query
            results.append(manager.alloc(val))
        else:                  # Erase query
            results.append(manager.erase(val))

    return results


# Example Usage:
initial_mem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queries = [[0, 2], [0, 5], [1, 1]]
print(solution(initial_mem, queries))
# Output: [0, 8, 2]