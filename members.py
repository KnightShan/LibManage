import pandas as pd

MEMBERS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\member.csv"

def add_new_member():
    try:
        mid = int(input("Enter Member ID: "))
        mname = input("Enter Member Name: ")
        phoneno = input("Enter Phone Number: ")
        numberofbooksissued = 0

        mdf = pd.read_csv(MEMBERS_CSV)
        n = mdf.shape[0]
        mdf.loc[n] = [mid, mname, phoneno, numberofbooksissued]
        mdf.to_csv(MEMBERS_CSV, index=False)

        print("✅ New member added successfully!")
        print(mdf.tail())
    except Exception as e:
        print("❌ Error adding member:", e)

def search_member():
    mname = input("Enter Member Name to Search: ")
    mdf = pd.read_csv(MEMBERS_CSV)
    result = mdf[mdf["m_name"].str.lower() == mname.lower()]
    
    if result.empty:
        print("🔍 No member found with the given name.")
    else:
        print("👤 Member Details:")
        print(result)

def delete_member():
    try:
        mid = int(input("Enter Member ID to Delete: "))
        mdf = pd.read_csv(MEMBERS_CSV)
        if mid in mdf["mid"].values:
            mdf = mdf[mdf["mid"] != mid]
            mdf.to_csv(MEMBERS_CSV, index=False)
            print("🗑️ Member deleted successfully.")
        else:
            print("❌ Member ID not found.")
    except Exception as e:
        print("❌ Error deleting member:", e)

def show_members():
    try:
        mdf = pd.read_csv(MEMBERS_CSV)
        if mdf.empty:
            print("📂 No members found.")
        else:
            print("👥 List of Members:")
            print(mdf)
    except Exception as e:
        print("❌ Error reading member file:", e)
