# 🚀 SQL & Pandas ELT With Global Standard

A lightweight, secure, and resource-efficient Extract, Load, Transform (ELT) and data analysis pipeline built with **Python**, **Pandas**, and **MariaDB**, specifically optimized for local development environments like **Vertual Machine (Crostini)**.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3
* **Data Manipulation & Analysis:** Pandas, SQLAlchemy
* **Database:** MariaDB (Local VM)
* **Visualization:** Plotly (Exported as high-res `.png` charts)
* **Security & Config:** `python-dotenv` for zero-hardcoded secret management
* **Version Control:** Git & GitHub

---

## 📂 Project Structure
```text
~/jupyter-work/
│
├── .env                  # Secure credentials (Ignored by Git)
├── .gitignore            # Excludes secrets, venv, and caches
├── cleanse_pipeline1.py  # Data cleaning and preprocessing script
├── import_to_db.py       # Load data into MariaDB
├── fetch_from_db.py      # Extract data from database
├── data_analyze_data.py  # Analytics, metrics, and chart generation
├── cleaned_orders.csv    # Intermediate clean dataset
├── quantity_by_product.png # Visual breakdown of unit sales
└── revenue_by_product.png  # Visual breakdown of total revenue

🔒 Security Best Practices
Zero Hardcoding: Database credentials (DB_USER, DB_PASS, DB_HOST, DB_NAME) are strictly managed using a local .env file.

Least Privilege Access: Connects to the database utilizing a dedicated db_worker role with read-only permissions.

Version Control Protection: The .env file and local virtual environment (jup_env/) are strictly excluded via .gitignore.

📊 Visualizations & Insights
1. Total Revenue by Product
Key Insight: The USB Hub dominates revenue generation, contributing significantly over $7,400 to the total top-line revenue due to its pricing and volume balance.

2. Quantity Sold by Product
Key Insight: USB Hub is also the top-selling product by unit volume (8 units sold), followed closely by Mouse and Webcam (5 units each).

🚀 Getting Started Locally
Clone the Repository:

Bash
git clone [https://github.com/faijulislam45f-netizen/sql_pandas_elt_pipeline.git](https://github.com/faijulislam45f-netizen/sql_pandas_elt_pipeline.git)
cd sql_pandas_elt_pipeline
Set up Virtual Environment:

Bash
python3 -m venv jup_env
source jup_env/bin/activate
Install Dependencies:

Bash
pip install pandas sqlalchemy pymysql python-dotenv plotly
Configure Environment Variables:
Create a .env file in the root directory:

Code snippet
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_NAME=tutorial_db
Run the Analysis Pipeline:

Bash
python3 data_analyze_data.py
