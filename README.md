# 🏥 OpenClaims — AI Claims Intelligence & Integrity Agent

> **An autonomous AI agent for healthcare claims sanitization, auditing & integrity**  
> Solves Privacy + Integrity challenges in medical claims data.

---

## 🧠 AI Agent Architecture

```mermaid
graph TB
    subgraph INPUT["📥 Raw Claims Data"]
        I1[837P EDI Files]
        I2[CSV Exports]
        I3[API Feeds]
    end

    subgraph AGENTS["🤖 AI Agent Suite"]
        A1[Sanitization Agent\nData De-identification]
        A2[Validation Agent\nFormat Verification]
        A3[Audit Rules Agent\nBusiness Logic Checks]
        A4[Report Generation\nAgent]
    end

    subgraph CHECKS["🔍 Audit Rule Engine"]
        C1[Financial: Billed >= Allowed >= Paid]
        C2[Clinical: Missing DX/CPT Codes]
        C3[Temporal: End Date >= Start Date]
        C4[Integrity: Member ID Consistency]
    end

    subgraph OUTPUT["📤 Deliverables"]
        O1[Clean Claims CSV]
        O2[Audit Report JSON]
        O3[Error Summary]
        O4[Financial Totals]
    end

    I1 --> A1
    I2 --> A1
    I3 --> A1
    A1 -->|Sanitized Data| A2
    A2 -->|Validated| A3
    A3 --> C1
    A3 --> C2
    A3 --> C3
    A3 --> C4
    C1 --> A4
    C2 --> A4
    C3 --> A4
    C4 --> A4
    A4 --> O1
    A4 --> O2
    A4 --> O3
    A4 --> O4

    style A1 fill:#4CAF50,stroke:#333,color:#fff
    style A3 fill:#2196F3,stroke:#333,color:#fff
    style A4 fill:#9C27B0,stroke:#333,color:#fff
    style C1 fill:#FF9800,stroke:#333,color:#fff
```

## 🤖 What the AI Agents Do

| Agent | Function |
|-------|----------|
| **Sanitization Agent** | Transforms sensitive claims data into de-identified datasets — preserves relationship integrity (same Patient ID = same fake name), generates realistic CPT/ICD-10/NPI codes |
| **Validation Agent** | Verifies data structure, required fields, and format compliance before audit |
| **Audit Rules Agent** | Runs 3 categories of business rules: Financial (billed ≥ allowed ≥ paid), Clinical (missing codes), Temporal (date logic) |
| **Report Agent** | Generates comprehensive audit reports with error logs and financial summaries |

## 🔄 Before vs After

```mermaid
graph LR
    subgraph BEFORE["❌ Before (Manual)"]
        BM[Spreadsheet review\nManual error checking\nHours per file\nHuman error risk]
    end

    subgraph AFTER["✅ After (AI Agent)"]
        AM[Automated sanitization\nInstant audit results\nMinutes per file\nZero compliance gaps]
    end

    BM -->|OpenClaims Agent| AM
```

## 🛠 Tech Stack

| Component | Technology | Agent Role |
|-----------|-----------|------------|
| **Sanitizer** | Python | Data de-identification engine |
| **Auditor** | Python | Rule-based validation engine |
| **Data** | CSV / JSON | Input/output formats |
| **Deployment** | Zero-dependency Python | Portable to any environment |

## ⚡ Quick Start

```bash
# 1. Generate mock claims data (HIPAA-safe)
python claims_sanitizer.py
# Output: mock_claims_data.csv (50+ columns)

# 2. Run the audit agent
python claims_auditor.py
# Output: Console summary + audit_report.json
```

## 💡 Why This Matters

**Payment Integrity** is a billion-dollar problem in the Payer/TPA space:
- **Auditing Skills:** Catches financial leakage (overpayments, duplicate billing)
- **Data Handling:** Comfortable with wide, complex datasets (DX codes, NPIs, Tax IDs)
- **Privacy First:** Deep HIPAA understanding — sanitization before any processing

---

Built by **[Shazaly Musa](https://github.com/SparkSpheartech)** — Founder, SparkSphear Tech  
*AI Agents for Healthcare Claims Integrity*