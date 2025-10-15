


# test_saver.py
from scripts.data_loader import load_csv
from scripts.data_cleaner import clean_data
from scripts.data_transformer import transform_data
from scripts.data_saver import save_to_csv

csv_path = "data/raw/raw_sales_data.csv"
schema_path = "schema/schema.json"

df = load_csv(csv_path, schema_path)
if df is not None:
    cleaned_df = clean_data(df)
    transformed_df = transform_data(cleaned_df)
    saved_path = save_to_csv(transformed_df)
    print(f"✅ File saved successfully at: {saved_path}")
else:
    print("❌ Failed to load CSV.")

