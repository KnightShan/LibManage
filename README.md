# LibManage - Library Management System

LibManage is a simple yet powerful Library Management System built in Python. It helps manage books, members, and book issuance/returns with a user-friendly command-line interface. The system uses CSV files for data storage and provides features for adding, searching, deleting, and viewing records, as well as generating basic charts.

---

## Features

- Add, search, delete, and display books
- Add, search, delete, and display members
- Issue and return books with date tracking
- View all issued books and delete issued records
- Basic visualization charts for:
  - Books and their cost
  - Number of books issued by members
- User authentication via username and password
- Data persistence using CSV files

---

## Technologies Used

- Python 3.10+
- Pandas (for CSV file handling and data manipulation)
- Matplotlib (for charts and visualization)
- CSV files for data storage

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/KnightShan/LibManage.git
   cd Library Management System

2. **Install dependencies**  
   Make sure you have Python 3.10+ installed. Then install required packages:
   ```bash
   pip install pandas matplotlib
   
3. **Prepare CSV files**  
   Create empty CSV files (book.csv, member.csv, issuebooks.csv, users.csv) in the project directory with the following headers:
   
   - book.csv:  
     bookid,title,author,publisher,edition,cost,category

   - member.csv:  
     mid,m_name,phoneno,numberofbooksissued

   - issuebooks.csv:  
     book_name,m_name,dateofissue,numberofbookissued,datereturn

   - users.csv:  
     username,password

 5. **Run the program**
    ```bash
    python main.py

  6. **Login**  
     Use credentials from users.csv to log in and start managing the library.


