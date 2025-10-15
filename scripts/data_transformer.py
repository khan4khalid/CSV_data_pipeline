import pandas as pd
from utils.logger import get_logger

logger = get_logger("DataTransformer")

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform feature engineering and transformations on the DataFrame.
    """
    logger.info("Starting data transformation...")

    # Example 1: Create new derived column (Yearly Bonus = 10% of salary)
    if "salary" in df.columns:
        df["yearly_bonus"] = df["salary"] * 0.10
        logger.info("Created 'yearly_bonus' as 10% of salary.")

    # Example 2: Categorize salary levels
    if "salary" in df.columns:
        df["salary_category"] = pd.cut(
            df["salary"],
            bins=[0, 30000, 70000, float("inf")],
            labels=["Low", "Medium", "High"]
        )
        logger.info("Added 'salary_category' column based on salary ranges.")

    # Example 3: Average salary per department (if column exists)
    if "department" in df.columns:
        dept_avg = df.groupby("department")["salary"].mean().reset_index()
        dept_avg.rename(columns={"salary": "avg_salary_by_dept"}, inplace=True)
        df = df.merge(dept_avg, on="department", how="left")
        logger.info("Added 'avg_salary_by_dept' using groupby merge.")

    logger.info("Data transformation completed successfully.")
    return df
 