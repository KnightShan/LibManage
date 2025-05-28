from auth import login
from books import addNewBook, searchBook, deleteBook, showBooks
from members import addNewMember, searchMember, deleteMember, showMembers
from issue_return import issueBooks, returnBook, showissuedBooks, deleteissuedBooks
from charts import showCharts

def showMenu():
    print("-----------------------------------------------------------------------")
    print("                      LIBRARY MANAGEMENT SYSTEM                        ")
    print("-----------------------------------------------------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - Delete an Issued Book Record")
    print("Press 13 - To View Charts")
    print("Press 14 - To Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    print("----------------------LIBRARY MANAGEMENT SYSTEM----------------------")
    if login():
        while True:
            ch = showMenu()
            if ch == 1:
                addNewBook()
            elif ch == 2:
                searchBook()
            elif ch == 3:
                deleteBook()
            elif ch == 4:
                showBooks()
            elif ch == 5:
                addNewMember()
            elif ch == 6:
                searchMember()
            elif ch == 7:
                deleteMember()
            elif ch == 8:
                showMembers()
            elif ch == 9:
                issueBooks()
            elif ch == 10:
                returnBook()
            elif ch == 11:
                showissuedBooks()
            elif ch == 12:
                deleteissuedBooks()
            elif ch == 13:
                showCharts()
            elif ch == 14:
                print("THANK YOU FOR VISITING THE LIBRARY")
                break
            else:
                print("Invalid Option Selected")
    else:
        print("Login failed. Exiting...")

if __name__ == "__main__":
    main()
