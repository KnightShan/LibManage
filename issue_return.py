import pandas as pd
from datetime import date

BOOKS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\book.csv"
MEMBERS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\member.csv"
ISSUE_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\issuebooks.csv"

def issue_book():
    book_name = input("Enter Book Name: ")
    books_df = pd.read_csv(BOOKS_CSV)
    if book_name not in books_df["title"].values:
        print("❌ Book not found in the library.")
        return

    member_name = input("Enter Member Name: ")
    members_df = pd.read_csv(MEMBERS_CSV)
    if member_name not in members_df["m_name"].values:
        print("❌ Member not found.")
        return

    try:
        number_of_books_issued = int(input("Enter number of books issued: "))
        issue_df = pd.read_csv(ISSUE_CSV)
        new_row = {
            "book_name": book_name,
            "m_name": member_name,
            "dateofissue": date.today(),
            "numberofbookissued": number_of_books_issued,
            "returndate": ""
        }
        issue_df.loc[len(issue_df)] = new_row
        issue_df.to_csv(ISSUE_CSV, index=False)

        print("✅ Book issued successfully!")
    except Exception as e:
        print("❌ Error issuing book:", e)

def return_book():
    member_name = input("Enter Member Name: ")
    book_name = input("Enter Book Name to Return: ")

    issue_df = pd.read_csv(ISSUE_CSV)
    condition = (issue_df["m_name"] == member_name) & (issue_df["book_name"] == book_name)

    if issue_df[condition].empty:
        print("❌ Book not issued to the given member.")
        return

    confirm = input("Are you sure you want to return the book? (yes/no): ").strip().lower()
    if confirm == "yes":
        issue_df = issue_df[~condition]
        issue_df.to_csv(ISSUE_CSV, index=False)
        print("✅ Book returned successfully.")
    else:
        print("ℹ️ Return cancelled.")

def show_issued_books():
    try:
        df = pd.read_csv(ISSUE_CSV)
        if df.empty:
            print("📂 No books are currently issued.")
        else:
            print("📘 Issued Books List:")
            print(df)
    except Exception as e:
        print("❌ Error reading issued books:", e)

def delete_issued_book():
    book_name = input("Enter Book Name to Delete from Issue Records: ")
    try:
        df = pd.read_csv(ISSUE_CSV)
        if book_name not in df["book_name"].values:
            print("❌ Book not found in issue records.")
            return
        df = df[df["book_name"] != book_name]
        df.to_csv(ISSUE_CSV, index=False)
        print("🗑️ Issued book record deleted successfully.")
    except Exception as e:
        print("❌ Error deleting issued book record:", e)
