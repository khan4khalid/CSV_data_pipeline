# CSV Data Pipeline

A modular **CSV ETL pipeline** built with Python for data engineering practice.  
This project demonstrates **loading, cleaning, transforming, validating, and saving CSV data** in a scalable and modular way.

<details>
  <summary>Project Structure</summary>


## Project Structure

csv_data_pipeline/
├── data/
│ ├── raw/ # Original CSV files
│ └── processed/ # Cleaned and transformed output
├── scripts/
│ ├── data_loader.py # Load CSV files into DataFrames
│ ├── data_cleaner.py # Clean missing values, duplicates, type conversions
│ ├── data_transformer.py # Transform columns, feature engineering, aggregations
│ ├── data_saver.py # Save cleaned data to CSV or database
├── utils/
│ ├── logger.py # Logger for all operations
│ └── schema_validator.py # Validate schema, check column names/types
├── main.py # Script to run full pipeline
└── requirements.txt # Project dependencies


</details>

## Features

- Load raw CSV data into Python **DataFrames**.
- Clean and transform datasets (handle **missing values, duplicates, type conversions, aggregations**).
- **Validate schema** before processing to ensure data consistency.
- Save processed data to **CSV** or **database**.
- Modular structure for **easy scalability**.
- **Logger** for tracking pipeline activities.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/csv_data_pipeline.git
cd csv_data_pipeline

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt