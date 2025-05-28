import pandas as pd
import matplotlib.pyplot as plt

BOOKS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\book.csv"
ISSUED_BOOKS_CSV = r"CC:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\issuebooks.csv"

def show_books_cost_chart():
    try:
        df = pd.read_csv(BOOKS_CSV)
        df = df[["title", "cost"]]
        df.plot(x="title", y="cost", kind="bar", legend=False, color="skyblue")
        plt.xlabel('Book Title')
        plt.ylabel('Cost')
        plt.title('Books and their Cost')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print(f"❌ '{BOOKS_CSV}' not found. Please ensure the file exists.")
    except Exception as e:
        print("❌ Error while plotting books cost chart:", e)


def show_issued_books_chart():
    try:
        df = pd.read_csv(ISSUED_BOOKS_CSV)
        # Group by member name and sum number of books issued
        grouped = df.groupby("m_name")["numberofbookissued"].sum().reset_index()
        grouped.plot(x="m_name", y="numberofbookissued", kind="bar", color="coral", legend=False)
        plt.xlabel('Member Name')
        plt.ylabel('Number of Books Issued')
        plt.title('Number of Books Issued by Members')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print(f"❌ '{ISSUED_BOOKS_CSV}' not found. Please ensure the file exists.")
    except Exception as e:
        print("❌ Error while plotting issued books chart:", e)


def show_charts():
    print("Press 1 - Books and their Cost")
    print("Press 2 - Number of Books issued by members")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_books_cost_chart()
    elif choice == '2':
        show_issued_books_chart()
    else:
        print("❌ Invalid choice selected.")
