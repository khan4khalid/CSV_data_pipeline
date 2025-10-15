# CSV Data Pipeline

## Project Overview

This project is a complete, modular ETL pipeline for handling CSV data.  
It demonstrates loading, cleaning, transforming, validating, and saving CSV datasets in Python, following best practices for data engineering projects.

- **ETL Features:**
    > Load raw CSV files into Python DataFrames  
    > Clean missing values, duplicates, and type conversions  
    > Transform columns and perform aggregations  
    > Validate schema before processing  
    > Save processed data to CSV or database  

## Tech Stack

- **Programming Language:** Python
- **Data Handling:** pandas, numpy
- **Logging:** Python logging module
- **Schema Validation:** Custom validator
- **Optional:** Database integration (SQLite/PostgreSQL)

## Folder Structure

csv_data_pipeline/\
│\
├── data/\
│   ├── raw/            # Original CSV files\
│   └── processed/      # Cleaned and transformed output\
│\
├── scripts/\
│   ├── data_loader.py      # Load CSV files into DataFrames\
│   ├── data_cleaner.py     # Clean missing values, duplicates, type conversions\
│   ├── data_transformer.py # Transform columns, feature engineering, aggregations\
│   └── data_saver.py       # Save cleaned data to CSV or database\
│\
├── utils/\
│   ├── logger.py           # Logger for all operations\
│   └── schema_validator.py # Validate schema, check column names/types\
│\
├── main.py                 # Script to run full pipeline\
└── requirements.txt        # Project dependencies

## Local Execution

You can run the pipeline in two ways: using a Python virtual environment or optionally integrating with a database.

### Using Python Virtual Environment

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/csv_data_pipeline.git
cd csv_data_pipeline

# 2. Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the pipeline
python main.py
