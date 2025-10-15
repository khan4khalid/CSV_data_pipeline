import pandas as pd
from utils.logger import get_logger

logger = get_logger("DataCleaner")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input DataFrame by handling missing values,
    removing duplicates, and fixing data types.
    """
    logger.info("Starting data cleaning...")

    # Step 1: Remove Duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info(f"Removed {before - after} duplicate rows.")

    # Step 2: Handle Missing Values
    missing = df.isnull().sum().sum()
    if missing > 0:
        logger.warning(f"Found {missing} missing values. Filling numeric with 0, string with 'Unknown'.")
        for col in df.columns:
            if df[col].dtype == "object":
                df[col].fillna("Unknown", inplace=True)
            else:
                df[col].fillna(0, inplace=True)
    else:
        logger.info("No missing values found.")

    # Step 3: Type Conversions
    if "salary" in df.columns:
        try:
            df["salary"] = df["salary"].astype(float)
            logger.info("Converted 'salary' column to float.")
        except Exception as e:
            logger.error(f"Error converting 'salary': {e}")

    logger.info("Data cleaning completed successfully.")
    return df
