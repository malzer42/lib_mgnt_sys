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

    message, set_message = use_state("")
    borrow_id, set_borrow_id = use_state("")
    borrow_quote, set_borrow_quote = use_state("")
    return_id, set_return_id = use_state("")
    return_quote, set_return_quote = use_state("")


    def handle_borrow(event):
        try:
            lib.borrow_book_by_subscriber(borrow_id, borrow_quote, 2025)
            set_message(f"Book {borrow_quote} borrowed by subscriber {borrow_id}.")
        except Exception as e:
            set_message(f"Error: {e}")

    def handle_return(event):
        try:
            lib.return_book_by_subscriber(return_id, return_quote)
            set_message(f"Book {return_quote} returned by subscriber {return_id}.")
        except Exception as e:
            set_message(f"Error: {e}")


    return html.div(
        {"style": {
            "fontFamily": "Arial",
            "padding": "20px",
            "maxWidth": "800px",
            "margin": "auto",
            "backgroundColor": "#f9f9f9",
            "border": "1px solid #ddd",
            "borderRadius": "8px"
        }},
        html.h1("📚 Library Inventory Management System"),
        html.h2("👤 Display the List of Subscribers"),
        html.ul(*subscribers_list),
        html.h2("📖  Diplay the List of Books"),
        html.ul(*books_list),
        html.h2("📚 👤 📖   Display the List of Borrow"),
        html.h2("🔄 Borrow a Book"),

        html.div(
                html.label("Subscriber ID: "),
                html.input({
                    "value": borrow_id,
                    "on_change": lambda e: set_borrow_id(e['target']['value']),
                    "style": {"padding": "5px", "marginBottom": "10px", "width": "200px"}
                })
            ),

        html.div(
                html.label("Book Quote: "),
                html.input({
                    "value": borrow_quote,
                    "on_change": lambda e: set_borrow_quote(e['target']['value']),
                    "style": {"padding": "5px", "marginBottom": "10px", "width": "200px"}
                })
            ),

        html.button(
            {"on_click": handle_borrow, "style": {"backgroundColor": "green", "color": "white", "padding": "10px"}},
                "Borrow Book"
            ),

        html.div(
            {"style": {"marginBottom": "20px", "marginTop": "20px"}},
            html.h2("↩️ Return a Book"),
            html.div(
                html.label("Subscriber ID: "),
                html.input({
                    "value": return_id,
                    "on_change": lambda e: set_return_id(e['target']['value']),
                    "style": {"padding": "5px", "marginBottom": "10px", "width": "200px"}
                })
            ),
            html.div(
                html.label("Book Quote: "),
                html.input({
                    "value": return_quote,
                    "on_change": lambda e: set_return_quote(e['target']['value']),
                    "style": {"padding": "5px", "marginBottom": "10px", "width": "200px"}
                })
            ),
            html.button(
                {"on_click": handle_return, "style": {"backgroundColor": "#007BFF", "color": "white", "padding": "10px"}},
                "Return Book"
            )
        ),

        html.div(
            html.h3("📋 Message Log",),
            html.div(message)
        ),

        html.div(
            html.h2("👤 Subscribers",),
            html.ul(*[html.li(s.info()) for s in lib.subscribers])
        ),

        html.div(
            html.h2("📖 Books" ),
            html.ul(*[html.li(b.info()) for b in lib.books])
        )   
    )

run(LMISDashboard)

