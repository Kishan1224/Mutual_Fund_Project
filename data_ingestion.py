import os
import pandas as pd

raw_data_folder = os.path.join("data", "raw")

csv_files = sorted(
    [file for file in os.listdir(raw_data_folder) if file.endswith(".csv")]
)

print(f"\nTotal datasets found: {len(csv_files)}")

for file_name in csv_files:

    file_path = os.path.join(raw_data_folder, file_name)

    try:
        df = pd.read_csv(file_path)

        print("\n" + "=" * 70)
        print(f"Dataset : {file_name}")

        print("\nShape")
        print(df.shape)

        print("\nColumn Data Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

    except Exception as error:
        print(f"\nUnable to read {file_name}")
        print(error)