# print option
from book import Book
import json

def print_options():
    print("press the specific button for that action")
    print("1-Create a new book")
    print("2-save books locally")
    print("3-load book from the disk ")
    print("5-return a book")
    print("6- show all books")
    print("7-show all the book")
    print("8-show book")
#crate_book_function
def input_book_info():
    id = input("ID: ")
    name = input("Name:")
    description = input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page Count: "))
    issued = input("Issued: y/Y for True anything else for False ")
    issued = (issued == "Y" or issued == "y")
    author = input("Author Name: ")
    year = int(input("Year"))
    return {
        'id': id,
        'name': name,
        'description': description,
        'isbn': isbn,
        'page_count': page_count,
        'issued': issued,
        'author': author,
        "year": year
    }


def create_book():
    print("Please enter your book information")
    book_input = input_book_info()
    book=Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'],
              book_input['issued'], book_input['author'], book_input['year'] )
    print(book.to_dict())
    return book
# defining save books
def save_books(books):
    json_books = []
    for books in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat", "w")
        file.write(json.dumps(json_books, indent = 4))
    except:
        print("we had an error saving books ")

def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
             new_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'],
                 book['issued'], book['author'], book['year'])
             books.append(new_obj)
        print("sucessfully loaded books")
        return books
    except:
        print("The file does not exist or an error occurred during loading")

        #find book function
        #takes books and id
        #if found returns the index of book in the books array, if not returns nothing
def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
        return None
def issue_book(books):
    id = input("enter the id of the book you want to issue")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully updated")
    else :
        print("could not find the book you are looking for ")

def return_book(books):
    id = input("enter the id of the book you want to Return :")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully Returned")
    else:
        print("could not find the book you are looking for ")

def update_book(books):
    id = input("Enter the Id of book you want to update ")
    index = find_book(books, id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated ")
    else:
        print("We could not find your book")
def show_all_books(books):
    for book in books:
        print(book.to.dict())

def show_book(books):
    id = input("please enter id of the book you are looking for :")
    index = find_book(books, id)
    if index != None:
        print(books[index].to.dict())
    else :
        print("We could not find the book you are looking for ")








