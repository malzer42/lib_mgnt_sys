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
    subscribers_list = [html.li(subscriber.info()) for subscriber in lib.subscribers]
    books_list = [html.li(book.info()) for book in lib.books]


    tab, set_tab = use_state("borrow")
    message, set_message = use_state("")
    borrow_id, set_borrow_id = use_state("")
    borrow_quote, set_borrow_quote = use_state("")
    return_id, set_return_id = use_state("")
    return_quote, set_return_quote = use_state("")
    sub_id, set_sub_id = use_state("")
    sub_first, set_sub_first = use_state("")
    sub_last, set_sub_last = use_state("")
    sub_age, set_sub_age = use_state("")
    book_quote, set_book_quote = use_state("")
    book_title, set_book_title = use_state("")
    book_year, set_book_year = use_state("")
    book_stock, set_book_stock = use_state("")
    book_avail, set_book_avail = use_state("")
    book_borrowed, set_book_borrowed = use_state("")
    search_input, set_search_input = use_state("")
    search_result, set_search_result = use_state([])

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

    def handle_add_subscriber(event):
        try:
            sub = Subscriber(sub_id, sub_first, sub_last, int(sub_age))
            lib.add_subscriber_to_library(sub)
            set_message(f"Added subscriber {sub_first} {sub_last}.")
        except Exception as e:
            set_message(f"Error: {e}")

    def handle_add_book(event):
        try:
            book = Book(book_quote, book_title, int(book_year), int(book_stock), int(book_avail), int(book_borrowed))
            lib.add_book_to_library(book)
            set_message(f"Added book '{book_title}'.")
        except Exception as e:
            set_message(f"Error: {e}")

    def handle_search(event):
        results = []
        for book in lib.books:
            if search_input.lower() in book.get_title.lower() or search_input.lower() in book.get_quote.lower():
                results.append(book.info())
        set_search_result(results or ["No matching books found."])

    tab_menu = html.div(
        {"style": {"marginBottom": "20px", "display": "flex", "gap": "10px"}},
        html.button({"on_click": lambda e: set_tab("borrow")}, "📖 Borrow/Return"),
        html.button({"on_click": lambda e: set_tab("add")}, "➕ Add Data"),
        html.button({"on_click": lambda e: set_tab("search")}, "🔍 Search"),
        html.button({"on_click": lambda e: set_tab("view")}, "📋 View All")
    )

    borrow_tab = html.div(
        html.h2("📖 Borrow or Return Book"),
        html.input({"placeholder": "Subscriber ID", "value": borrow_id, "on_change": lambda e: set_borrow_id(e['target']['value'])}),
        html.input({"placeholder": "Book Quote", "value": borrow_quote, "on_change": lambda e: set_borrow_quote(e['target']['value'])}),
        html.button({"on_click": handle_borrow}, "Borrow"),
        html.hr(),
        html.input({"placeholder": "Subscriber ID", "value": return_id, "on_change": lambda e: set_return_id(e['target']['value'])}),
        html.input({"placeholder": "Book Quote", "value": return_quote, "on_change": lambda e: set_return_quote(e['target']['value'])}),
        html.button({"on_click": handle_return}, "Return")
    )

    add_tab = html.div(
        html.h2("➕ Add Subscriber"),
        html.input({"placeholder": "ID", "value": sub_id, "on_change": lambda e: set_sub_id(e['target']['value'])}),
        html.input({"placeholder": "First Name", "value": sub_first, "on_change": lambda e: set_sub_first(e['target']['value'])}),
        html.input({"placeholder": "Last Name", "value": sub_last, "on_change": lambda e: set_sub_last(e['target']['value'])}),
        html.input({"placeholder": "Age", "value": sub_age, "on_change": lambda e: set_sub_age(e['target']['value'])}),
        html.button({"on_click": handle_add_subscriber}, "Add Subscriber"),
        html.hr(),
        html.h2("📘 Add Book"),
        html.input({"placeholder": "Quote", "value": book_quote, "on_change": lambda e: set_book_quote(e['target']['value'])}),
        html.input({"placeholder": "Title", "value": book_title, "on_change": lambda e: set_book_title(e['target']['value'])}),
        html.input({"placeholder": "Year", "value": book_year, "on_change": lambda e: set_book_year(e['target']['value'])}),
        html.input({"placeholder": "Stock", "value": book_stock, "on_change": lambda e: set_book_stock(e['target']['value'])}),
        html.input({"placeholder": "Available", "value": book_avail, "on_change": lambda e: set_book_avail(e['target']['value'])}),
        html.input({"placeholder": "Borrowed", "value": book_borrowed, "on_change": lambda e: set_book_borrowed(e['target']['value'])}),
        html.button({"on_click": handle_add_book}, "Add Book")
    )

    search_tab = html.div(
        html.h2("🔍 Search Books"),
        html.input({"placeholder": "Enter title or quote", "value": search_input, "on_change": lambda e: set_search_input(e['target']['value'])}),
        html.button({"on_click": handle_search}, "Search"),
        html.ul(*[html.li(result) for result in search_result])
    )

    view_tab = html.div(
        html.h2("👤 Subscribers"),
        html.ul(*[html.li(s.info()) for s in lib.subscribers]),
        html.h2("📖 Books"),
        html.ul(*[html.li(b.info()) for b in lib.books])
    )

    tab_content = {
        "borrow": borrow_tab,
        "add": add_tab,
        "search": search_tab,
        "view": view_tab
    }

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
        html.h1("📚 Library Inventory Management System Multi-Tab GUI"),
        tab_menu,
        html.div(tab_content[tab]),
        html.hr(),
        html.div(html.b("Message: "), message)
    )

run(LMISDashboard)
