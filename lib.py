# Create Library class
class Library:

    def __init__(self):
       
        # Store books in dictionary
        self.books = {
            "harry potter": {
                "author": "J.K. Rowling",
                "description": "Story of a young wizard."
            },

            "you can win": {
                "author": "Shiv khera",
                "description": "is a motivational book that teaches positive thinking"
            },

            "sham chi aai": {
                "author": "sane guruji",
                "description": "story of mother love"
            },

            "chhava": {
                "author": "shivaji Sawant",
                "description": "based on Chh. Sambhaji Maharaj"
            },

            "rich dad poor dad": {
                "author": "Robert Kiyosaki",
                "description": "Learn money management."
            }
        }

    # Function to search book
    def find_book(self, name):
        

        # Check if book exists
        if name in self.books:

            print("\nBook Found")
            print("Book Name :", name)
            print("Author :", self.books[name]["author"])
            print("Description :", self.books[name]["description"])

        else:
            print("\nBook not found")


# Create object
lib = Library()

# Take input from user
book_name = input("Enter book name: ")

# Search book
lib.find_book(book_name)