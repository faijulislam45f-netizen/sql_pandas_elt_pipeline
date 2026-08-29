# SQL & Pandas ETL Pipeline (Industry Standard)

A lightweight, secure, and resource-efficient Extract, Load, Transform (ETL) and data analysis pipeline built with Python, Pandas, and MariaDB, specifically optimized for local development environments like **Machine (Linux VM)**.

---

## 📊 Pipeline Overview

| Detail | Info |
| :--- | :--- |
| **Source** | Local MariaDB (`tutorial_db`) |
| **Output** | `cleaned_orders.csv` |
| **Rows Analyzed** | 8 (Executive Summary Sample) |
| **Focus** | Sales Revenue & Volume Analysis |
| **Security** | Zero-hardcoded credentials (`.env`) |

---

## 🔑 Key Findings

* **Total Revenue** generated across the analyzed sample is **$15,535.14**.
* **Average Order Value (AOV)** stands at a healthy **$1,941.89**.
* **USB Hub** is the absolute top performer, dominating both **Revenue (>$7,400)** and **Quantity Sold (8 units)**.
* Pipeline successfully executes secure end-to-end data extraction and transformation with **zero credential leakage**.

---

## 📈 Visualizations

### Total Revenue by Product
![Total Revenue](https://raw.githubusercontent.com/faijulislam45f-netizen/sql_pandas_elt_pipeline/main/revenue_by_product.png)

### Quantity Sold by Product
![Quantity Sold](https://raw.githubusercontent.com/faijulislam45f-netizen/sql_pandas_elt_pipeline/main/quantity_by_product.png)

---

## 🧹 Data Security & Processing

* **Zero Hardcoding**: Credentials (`DB_USER`, `DB_PASS`) safely managed using `python-dotenv`.
* **Access Control**: Database connection utilizes a restricted `db_worker` role with read-only permissions.
* **Git Protection**: `.env` and `jup_env/` are strictly ignored via `.gitignore` to prevent secret leaks.
* **Automation**: Charts and aggregated metrics are auto-generated via Python scripts using `.groupby()`.

---

## 📋 Executive Summary Metrics

| Metric | Value |
| :--- | :--- |
| **Total Revenue** | $15,535.14 |
| **Avg Order Value (AOV)** | $1,941.89 |
| **Top Product (Qty)** | USB Hub (8 units) |
| **Top Product (Revenue)** | USB Hub (>$7,400) |

---

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `import_to_db.py` | Load raw data into MariaDB |
| `fetch_from_db.py` | Securely extract data from the database |
| `cleanse_pipeline1.py` | Data cleaning and preprocessing script |
| `data_analyze_data.py` | Aggregates metrics & generates Plotly charts |
| `cleaned_orders.csv` | Intermediate clean dataset output |
| `revenue_by_product.png` | Exported Bar Chart — Revenue |
| `quantity_by_product.png` | Exported Bar Chart — Quantity |

---

## 🛠️ Tools Used

`Python` `Pandas` `MariaDB` `SQLAlchemy` `Plotly` `Dotenv`

---

## 💡 Skills Demonstrated

* End-to-end ELT Pipeline Architecture
* Secure Credential Management & Git Best Practices
* Relational Database (MariaDB) Integration
* Data Aggregation & Business Logic in Pandas
* Programmatic Data Visualization with Plotly
