
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None

    def __str__(self):
        borrowed_status = f"Yes, by {self.borrowed_by}" if self.is_borrowed else "No"
        return (f"Title: {self.title}, "
                f"Author: {self.author}, "
                f"ISBN: {self.isbn}, "
                f"Borrowed: {borrowed_status}")


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, isbn, user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist.")
            return

        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrowed_by = user_id
                    print(
                        f"User: {self.users[user_id].name} "
                        f"has borrowed '{book.title}'."
                    )
                else:
                    print(f"Book '{book.title}' has already been borrowed.")
                return

        print("Book not found in the library.")

    def add_user(self, user):
        if user.user_id in self.users:
            print(f"User ID {user.user_id} already exists.")
            return
        self.users[user.user_id] = user
        print(f"User '{user.name}' added with ID {user.user_id}.")

    def list_users(self):
        if not self.users:
            print("No users registered.")
            return
        for user_id, user in self.users.items():
            print(user)

    def update_user(self, user_id, name=None, email=None):
        if user_id not in self.users:
            print("User not found.")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User '{user_id}' updated.")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted.")
        else:
            print("User not found.")

    def return_book(self, isbn, user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist.")
            return

        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed and book.borrowed_by == user_id:
                    book.is_borrowed = False
                    book.borrowed_by = None
                    print(
                        f"User: {self.users[user_id].name} "
                        f"has returned '{book.title}'."
                    )
                else:
                    print("Book is not borrowed by this user.")
                return

        print("Book not found in the library.")


book1 = Book("Python Crash Course", "Eric Matthes", "1593279280")
book2 = Book("Automate the Boring Stuff With Python",
             "Al Sweigart", "1593279922")
book3 = Book("Effective Java", "Joshua Bloch", "0135685997")
book4 = Book("The Pragmatic Programmer",
             "Andrew Hunt and David Thomas", "01359577052")

print(book1)
print(book3)

print()

library = Library()

print()

library.list_books()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.add_book(Book("Learn Java", "Jane Doe", "9876543210"))

print()

library.list_books()

print()

library.add_user(User("001", "John Doe", "johndoe@example.com"))
library.add_user(User("002", "Jane Smith", "janesmith@example.com"))

print()

library.borrow_book("01359577052", "001")
library.borrow_book("1593279922", "002")
library.borrow_book("1593279280", "001")
library.borrow_book("01359577052", "002")
library.borrow_book("01357952", "001")

print(book4)

print()

library.return_book("01359577052", "001")
library.return_book("1593279922", "002")
library.return_book("1593279280", "001")
library.return_book("01359577052", "002")

print(book4)

print()

library.list_users()

print()

library.update_user("001", name="Johnathan Doe",
                    email="update@example.com")
library.update_user("002", email="onlynewemail@example.com")

print()

library.list_users()

print()

library.delete_user("001")

print()

library.list_users()
