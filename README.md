# Automated E-Commerce Data Ingestion Pipeline & Analytics Engine

An end-to-end data engineering pipeline designed to dynamically extract, parse, clean, and structure unstructured data from complex, JavaScript-rendered e-commerce platforms (including Daraz and other marketplaces).

## Key Features & Architecture
- Dynamic Web Orchestration:** Leverages Selenium WebDriver to handle asynchronous content loading, infinite scrolling, and multi-page pagination natively.
- Targeted Data Extraction:** Extracts deep product attributes including pricing structures, customer ratings, product names, and stock metrics (e.g., focused on consumer electronics and smartphones).
- Data Transformation & Structuring:** Utilizes the Pandas framework to process raw extracted strings, normalize unstructured text, and clean data irregularities into deterministic tabular schemas.
- Downstream Export:** Automated parsing into optimized data formats (`.xlsx` / `.csv`) via Pandas DataFrames for immediate analytic consumption.

## Tech Stack
- Language: Python 3
- Automation Framework: Selenium WebDriver
- Data Engineering & Manipulation: Pandas, NumPy
- Storage/Output Engine: OpenPyXL (Excel integration)
