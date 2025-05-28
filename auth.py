import pandas as pd

USERS_CSV = r"C:\Users\Shantanu\OneDrive\Desktop\Project X\Library Management System\Data\users.csv"

def login():
    print("🔐 Login to Library Management System")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        df = pd.read_csv(USERS_CSV)

        user = df.loc[(df["username"] == username) & (df["password"] == password)]

        if not user.empty:
            print("✅ Login successful. Welcome,", username)
            return True
        else:
            print("❌ Invalid username or password.")
            return False

    except FileNotFoundError:
        print(f"❌ '{USERS_CSV}' not found. Please ensure the file exists.")
        return False
    except Exception as e:
        print("❌ An error occurred during login:", e)
        return False
