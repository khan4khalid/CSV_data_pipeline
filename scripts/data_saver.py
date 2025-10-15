import os
import pandas as pd
from utils.logger import get_logger

logger = get_logger("DataSaver")

def save_to_csv(df: pd.DataFrame, output_dir: str = "data/processed", file_name: str = "cleaned_data.csv") -> str:
    """
    Saves the DataFrame to a CSV file in the specified output directory.
    Returns the file path.
    """
    logger.info("Starting data saving process...")

    # Ensure directory exists
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, file_name)
    df.to_csv(output_path, index=False)
    
    logger.info(f"Data saved successfully at: {output_path}")
    return output_path
