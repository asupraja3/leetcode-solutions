class Library:
    def __init__(self):
        # Dictionary to store book_id -> popularity
        self.books = {}

    def add_book(self, book_id, popularity):
        """Adds a new book with the given ID and popularity."""
        self.books[book_id] = popularity

    def update_popularity(self, book_id, new_popularity):
        """Updates the popularity score of an existing book."""
        if book_id in self.books:
            self.books[book_id] = new_popularity

    def get_top_n(self, n):
        """Retrieves the top N most popular book IDs."""
        # Sort books by popularity (score) in descending order
        # key=lambda x: x[1] looks at the score
        sorted_books = sorted(self.books.items(), key=lambda x: x[1], reverse=True)
        
        # Return only the book IDs of the top N books
        return [book_id for book_id, score in sorted_books[:n]]

# --- Driver Code to match the Input format in the image ---
def run_operations(operations):
    library = Library()
    output = []

    for op in operations:
        command = op[0]
        
        if command == 'add':
            # op[1] is ID, op[2] is popularity
            library.add_book(op[1], op[2])
            
        elif command == 'update':
            # op[1] is ID, op[2] is new popularity
            library.update_popularity(op[1], op[2])
            
        elif command == 'top':
            # op[1] is N
            result = library.get_top_n(op[1])
            output.append(result)
            
    return output

# --- Example Usage based on your screenshot ---
inputs = [
    ['add', '101', 5],
    ['add', '102', 10],
    ['add', '103', 3],
    ['top', 2],
    ['update', '101', 12],
    ['top', 2]
]

print(run_operations(inputs))