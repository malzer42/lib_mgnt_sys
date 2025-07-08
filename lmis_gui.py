from reactpy import component, html, run, use_state
from subscriber import Subscriber
from book import Book
from library import Library

# Initialize the library with some data
lib = Library([], 0, [], 0, [], 0)

# Preload sample data
subscribers_list = [
    Subscriber("1839456", "John", "Doe", 23),
    Subscriber("1630236", "Nicolas", "Gagnon", 8),
    Subscriber("1269348", "Martin", "Tremblay", 18)
]

books_list = [
    Book("HB514", "Bjh D++", 2010, 9, 3, 4),
    Book("GA403", "Big C++", 2009, 8, 3, 3),
    Book("QA203", "Calcul Partie 1", 2011, 3, 2, 2),
    Book("QA204", "Calcul Partie 2", 2011, 3, 2, 2),
    Book("AC409", "Le chateau d'Ortrante", 1764, 16, 1, 1),
    Book("BD302", "Harry Potter et le prisonier d'Azkaban", 1999, 3, 1, 1),
    Book("CE413", "Ibssz Qpuufs et le prisonier c'balbcbo", 2000, 4, 2, 2)
]

for subscriber in subscribers_list:
    lib.add_subscriber_to_library(subscriber)

for book in books_list:
    lib.add_book_to_library(book)



@component
def LMISDashboard():
    subscribers_list = [html.li(sub.info()) for sub in lib.subscribers]
    books_list = [html.li(book.info()) for book in lib.books]

    return html.div(
        html.h1("📚 Library Inventory Management System"),
        html.h2("👤 Display the List of Subscribers"),
        html.ul(*subscribers_list),
        html.h2("📖  Diplay the List of Books"),
        html.ul(*books_list)
    )

run(LMISDashboard)

