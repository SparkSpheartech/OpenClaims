# OpenClaims - Claims Intelligence & Integrity Engine

**OpenClaims** is a Python-based toolkit designed to solve two critical challenges in healthcare data: **Privacy** and **Integrity**.

It demonstrates the ability to handle complex medical claims data, anonymize it for safe usage (Sanitization), and automatically audit it for financial and logical errors (Auditing).

## 🚀 Key Features

*   **Claims Sanitizer**: A robust engine that takes raw, sensitive claims data (like 837P or custom CSV exports) and transforms it into strict, de-identified datasets.
    *   *Preserves Logic*: Maintains relationship integrity (Same Patient ID = Same Fake Name).
    *   *Realistic Data*: Generates valid CPT codes, ICD-10 diagnosis codes, and NPI-like provider IDs.
*   **Audit Rules Engine**: An automated quality gate that runs business rules against claims.
    *   *Financial Checks*: Validates that `Billed` >= `Allowed` >= `Paid`.
    *   *Clinical Logic*: Checks for missing Diagnosis or Procedure codes.
    *   *Temporal Logic*: Ensures Service End Date is not before Start Date.
*   **Zero Dependencies**: Built entirely with standard Python libraries for maximum portability and security.

## 🛠 Project Structure

*   `claims_sanitizer.py`: The data generation engine. It creates high-fidelity mock data that mimics real-world TPA/Payer exports.
*   `claims_auditor.py`: The validation engine. It reads the claims, applies a rule set, and outputs a quality report.
*   `mock_claims_data.csv`: (Generated) The complex input dataset.
*   `audit_report.json`: (Generated) A summary of data quality, financial totals, and error logs.

## ⚡ How to Run

### 1. Generate Mock Claims
Create a clean, privacy-safe dataset.
```bash
python claims_sanitizer.py
```
*Output: `mock_claims_data.csv` (contains ~50 columns of complex medical/financial data)*

### 2. Run the Auditor
Scan the data for errors and generate a report.
```bash
python claims_auditor.py
```
*Output: Console summary + `audit_report.json`*

## 💡 Why this Matters
In the Payer/TPA space, **Payment Integrity** is a billion-dollar problem.
*   **Auditing Skills**: This project proves you can write code to catch financial leakage (overpayments).
*   **Data Handling**: Demonstrates comfort with wide, complex datasets (Diagnosis codes, NPIs, Tax IDs).
*   **Privacy First**: Shows deep understanding of HIPAA constraints by prioritizing sanitization.

---
*Created by Shazaly Musa*
