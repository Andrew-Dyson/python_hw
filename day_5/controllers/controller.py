from flask import redirect, request, render_template

from app import app
from models.book import Book
from models.books import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def books_index():
    return render_template("books.html", books=book_list)

@app.route("/books/<index>")
def show_book(index):
    book = book_list[int(index)]
    return render_template("book.html", book=book, index=index)

# @app.route("/books", methods=["POST"])
# def post_book():
#     if request.form["title"] != "":
#         book_title = request.form["title"]
#         book_author = request.form["author"]
#         book_genre = request.form["genre"]
#         added_book = Book(book_title, book_author, book_genre, False)
#         add_book(added_book)
#     elif request.form["index"] != "":
#         index = request.form["index"]
#         remove_book(int(index))
#     return redirect("/books")

@app.route('/books', methods=['POST'])
def post_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    added_book = Book(book_title, book_author, book_genre, False)
    add_book(added_book)
    return redirect("/books")
    
@app.route("/books/addform")
def books_addform():
    return render_template("addform.html")


# @app.route('/books/<index>', methods=['POST'])
# def books_delete(index):
#     index = request.form["index"]
#     remove_book(int(index))
#     return redirect("/books")

# @app.route('/books/<index>', methods=['POST'])
# def books_delete(index):
#     index = request.form["index"]
#     remove_book(int(index))
#     return redirect("/books")

@app.route('/books/<index>', methods=['POST'])
def book_check_out(index):
    index = request.form["index"]
    check_out_book(book_list[int(index)])
    return redirect("/books")

# @app.route("/books/<index>", methods=["POST"])
# def books_update(index):
#     book = book_list[int(index)]
#     checked_out = "check_out" in request.form
#     book.toggle_check_out(checked_out)
#     return redirect("/books/" + index)
    