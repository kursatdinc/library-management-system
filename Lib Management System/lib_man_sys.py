class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if books:
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")
        else:
            print("No books available.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book you want to remove: ")
        updated_books = []
        self.file.seek(0)
        for line in self.file:
            book_info = line.strip().split(',')
            if book_info[0] != title_to_remove:
                updated_books.append(line)
        self.file.seek(0)
        self.file.truncate()
        for book in updated_books:
            self.file.write(book)
        print("Book removed successfully.")


def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()