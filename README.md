# CSV Data Pipeline

A modular CSV ETL pipeline built with Python for data engineering practice.
Project Structure : 

csv_data_pipeline/
│
├── data/
│ ├── raw/ # Original CSV files
│ └── processed/ # Cleaned and transformed output
│
├── scripts/
│ ├── data_loader.py # Load CSV files into DataFrames
│ ├── data_cleaner.py # Clean missing values, duplicates, type conversions
│ ├── data_transformer.py # Transform columns, feature engineering, aggregations
│ ├── data_saver.py # Save cleaned data to CSV or database
│
├── utils/
│ ├── logger.py # Logger for all operations
│ └── schema_validator.py # Validate schema, check column names/types
│
├── main.py # Script to run full pipeline
└── requirements.txt # Project dependencies

Features

- Load raw CSV data into Python DataFrames.
- Clean and transform datasets (missing values, duplicates, type conversions, aggregations).
- Validate schema before processing.
- Save processed data to CSV or database.
- Modular structure for easy scalability.
- Logger for tracking pipeline activities.



Installation

Clone the repo:

bash
git clone https://github.com/<your-username>/csv_data_pipeline.git
cd csv_data_pipeline
