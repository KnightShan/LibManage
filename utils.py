import pandas as pd

def read_csv_file(filepath):
    """Read a CSV file into a pandas DataFrame safely."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except pd.errors.EmptyDataError:
        print(f"❌ File is empty: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return None

def write_csv_file(df, filepath):
    """Write a pandas DataFrame to CSV file safely."""
    try:
        df.to_csv(filepath, index=False)
        print(f"✅ Successfully saved data to {filepath}")
    except Exception as e:
        print(f"❌ Error saving to {filepath}: {e}")

def append_row_to_df(df, row):
    """Append a row (list or dict) to a DataFrame and return new DataFrame."""
    if isinstance(row, dict):
        new_df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    elif isinstance(row, list):
        # assuming row list order matches df.columns
        new_df = df.append(pd.Series(row, index=df.columns), ignore_index=True)
    else:
        raise ValueError("Row must be a dict or list")
    return new_df
