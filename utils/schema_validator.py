import json
import pandas as pd
from utils.logger import get_logger

logger = get_logger("SchemaValidator")

def validate_schema(csv_path: str, schema_path: str) -> bool:
    """
    Validates CSV file against schema definition.
    Returns True if valid, False otherwise.
    """

    logger.info(f"Validating schema for file: {csv_path}")

    try:
        # Load schema
        with open(schema_path, "r") as f:
            schema = json.load(f)
        expected_cols = schema["columns"]

        # Load CSV
        df = pd.read_csv(csv_path)
        csv_cols = df.columns.tolist()

        # Check for missing or extra columns
        missing_cols = [col for col in expected_cols if col not in csv_cols]
        extra_cols = [col for col in csv_cols if col not in expected_cols]

        if missing_cols:
            logger.error(f"Missing columns: {missing_cols}")
            return False

        if extra_cols:
            logger.warning(f"Extra columns found: {extra_cols}")

        # Check data types
        for col, expected_dtype in expected_cols.items():
            if col in df.columns:
                actual_dtype = str(df[col].dtype)
                if expected_dtype != actual_dtype:
                    logger.warning(f"Column '{col}' has dtype '{actual_dtype}', expected '{expected_dtype}'")

        logger.info("✅ Schema validation passed successfully.")
        return True

    except Exception as e:
        logger.error(f"Schema validation failed: {e}")
        return False
