import pandas as pd

BOOKS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\book.csv"

def add_new_book():
    try:
        bookid = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        publisher = input("Enter Publisher Name: ")
        edition = input("Enter Edition: ")
        cost = int(input("Enter Book Cost: "))
        category = input("Enter Book Category: ")

        bdf = pd.read_csv(BOOKS_CSV)
        n = bdf.shape[0]
        bdf.loc[n] = [bookid, title, author, publisher, edition, cost, category]
        bdf.to_csv(BOOKS_CSV, index=False)

        print("✅ Book added successfully!")
        print(bdf.tail())
    except Exception as e:
        print("❌ Error adding book:", e)

def search_book():
    title = input("Enter Book Title to Search: ")
    bdf = pd.read_csv(BOOKS_CSV)
    result = bdf[bdf["title"].str.lower() == title.lower()]
    
    if result.empty:
        print("🔍 No book found with the given title.")
    else:
        print("📖 Book Details:")
        print(result)

def delete_book():
    try:
        bookid = int(input("Enter Book ID to Delete: "))
        bdf = pd.read_csv(BOOKS_CSV)
        if bookid in bdf["bookid"].values:
            bdf = bdf[bdf["bookid"] != bookid]
            bdf.to_csv(BOOKS_CSV, index=False)
            print("🗑️ Book deleted successfully.")
        else:
            print("❌ Book ID not found.")
    except Exception as e:
        print("❌ Error deleting book:", e)

def show_books():
    try:
        bdf = pd.read_csv(BOOKS_CSV)
        if bdf.empty:
            print("📂 No books in the library.")
        else:
            print("📚 List of Books:")
            print(bdf)
    except Exception as e:
        print("❌ Error reading book file:", e)
