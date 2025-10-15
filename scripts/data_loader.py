import pandas as pd
from utils.logger import get_logger
from utils.schema_validator import validate_schema

logger = get_logger("DataLoader")

def load_csv(csv_path: str, schema_path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a DataFrame after schema validation.
    Returns DataFrame if successful, otherwise None.
    """
    logger.info(f"Attempting to load CSV: {csv_path}")

    # Step 1: Validate Schema
    if not validate_schema(csv_path, schema_path):
        logger.error("Schema validation failed. File will not be loaded.")
        return None

    try:
        # Step 2: Load Data
        df = pd.read_csv(csv_path)
        logger.info(f"CSV loaded successfully with {len(df)} rows and {len(df.columns)} columns.")
        return df

    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
        return None

    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        return None
