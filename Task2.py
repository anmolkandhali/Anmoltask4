class BookInfo:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_author

class BookManager:
    def __init__(self):
        self.collection = []

    def insert_book(self, new_entry):
        self.collection.append(new_entry)
        print(f"Book '{new_entry.book_title}' by {new_entry.book_author} added successfully.")

    def display_books(self):
        if len(self.collection) == 0:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for number, item in enumerate(self.collection, 1):
                print(f"{number}. {item.book_title} by {item.book_author}")

def run_library_app():
    manager = BookManager()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Exit")

        user_input = input("Enter your choice (1-3): ")

        if user_input == '1':
            title_input = input("Enter book title: ")
            author_input = input("Enter author name: ")
            entry = BookInfo(title_input, author_input)
            manager.insert_book(entry)

        elif user_input == '2':
            manager.display_books()

        elif user_input == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

run_library_app()