# 🚀 SQL & Pandas ELT on Linux VM Machine Global Standard Pipeline

A lightweight, secure, and resource-efficient Extract, Load, Transform (ELT) and data analysis pipeline built with **Python**, **Pandas**, and **MariaDB**, specifically optimized for local development environments like **Chromebook Linux (Crostini)**.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3
* **Data Manipulation & Analysis:** Pandas, SQLAlchemy
* **Database:** MariaDB (Local VM)
* **Visualization:** Plotly (Exported as high-res `.png` charts)
* **Security & Config:** `python-dotenv` for zero-hardcoded & Secure credential management
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
