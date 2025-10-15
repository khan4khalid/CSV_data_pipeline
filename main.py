from scripts.data_loader import load_csv
from scripts.data_cleaner import clean_data
from scripts.data_transformer import transform_data
from scripts.data_saver import save_to_csv
from utils.schema_validator import validate_schema
from utils.logger import get_logger

logger = get_logger("MainPipeline")

RAW_CSV_PATH = "data/raw/raw_sales_data.csv"
SCHEMA_PATH = "schema/schema.json"

def run_pipeline():
    logger.info("=== ETL Pipeline Started ===")
    
    # Step 1: Load CSV
    df = load_csv(RAW_CSV_PATH,SCHEMA_PATH)
    if df is None:
        logger.error("Pipeline stopped: Failed to load CSV.")
        return
    
    # Step 2: Validate schema
    if not validate_schema(df, SCHEMA_PATH):
        logger.warning("Schema validation failed. Proceeding with caution.")
    
    # Step 3: Clean data
    df_clean = clean_data(df)
    
    # Step 4: Transform data
    df_transformed = transform_data(df_clean)
    
    # Step 5: Save processed data
    save_to_csv(df_transformed)
    
    logger.info("=== ETL Pipeline Completed Successfully ===")

if __name__ == "__main__":
    run_pipeline()
