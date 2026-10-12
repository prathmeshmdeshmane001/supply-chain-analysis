# Supply Chain Logistics Optimization & Predictive SLA Risk Engine
### An End-to-End Analytics & Machine Learning Pipeline for Delivery Reliability and Margin Defense

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/prathmeshmdeshmane001/supply-chain-analysis)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?logo=python)](https://python.org)
[![Status](https://img.shields.io/badge/Pipeline-Verified%20%26%20Active-success)](#)

---

## 1. Executive Summary: The PM & Supply Chain Manager POV

### The Business Problem
In e-commerce and retail supply chains, **customer retention lives and dies on delivery promise reliability**. If an order misses its promised Delivery Date (EDD), customer satisfaction plunges, "Where Is My Order?" (WISMO) support ticket volume spikes, and long-term Customer Lifetime Value (LTV) is severely eroded.

In this enterprise supply chain dataset of **172,765 fulfillment orders**:
- **54.71% of orders suffer delivery delays** (an On-Time Fulfillment rate of only **45.29%**).
- **$2,055,765 in order profit is tied to delayed shipments**, directly risking margin loss through refund concessions and churn.
- **18.69% of all fulfilled orders operate at a net negative margin (loss)**, showing a critical need for fulfillment profitability controls.

### The Product & Operational Objective
As a **Supply Chain Manager / Product Manager (Fulfillment & Logistics Tech)**, our objective is threefold:
1. **Diagnose Friction Points**: Pinpoint the geographic corridors, shipping tiers, and product departments driving late deliveries.
2. **Quantify Financial Risk**: Map delivery delays against gross margin leakage to justify operational logistics spend.
3. **Deploy a Predictive Dispatch Engine**: Build and integrate a pre-dispatch Machine Learning classifier (Random Forest with SMOTE) into the Order Management System (OMS) to flag high-risk shipments at checkout with **78% precision**, enabling dynamic carrier upgrades and promise date adjustments.

---

## 2. Supply Chain & Product KPI Dashboard

```text
========================================================================================
                          SUPPLY CHAIN MANAGEMENT SCORECARD
========================================================================================
Total Orders Evaluated (Cleaned)        :  172,765
On-Time Fulfillment Rate (OTIF)         :  45.29%  (Industry Benchmark: >85-95%)
SLA Breach / Late Delivery Rate         :  54.71%  (94,523 orders breached SLA)
90th Percentile Lead Time Buffer (P90)  :  3.00 days
Most Common Delay Cohort                :  +1 Day (30.97% of all orders)
Total Gross Profit Realized             :  $7,514,813.81 (~$7.5M)
Profit Volume Exposed to Late Delivery  :  $2,055,765.16 (~$2.1M / 27.4% of total profit)
Net Negative Margin Orders (Losses)     :  32,295 orders (18.69% of fulfillment volume)
========================================================================================
```

---

## 3. Product Manager & Supply Chain Insights

### 3.1. The "1-to-2 Day" Delivery Promise Trap
- **Analysis**: Over **46.9% of all orders arrive either 1 or 2 days late** (+1 day: 30.97%, +2 days: 15.95%). Only 7.8% of orders experience extreme delays of 3 or 4 days.
- **PM Takeaway**: This is **not a cataclysmic transit breakdown**; it is a **static scheduling mismatch**. The checkout promise engine is promising delivery windows that are 24–48 hours tighter than 3PL carriers can fulfill.
- **Action**: Implementing an automated buffer (+1 to +2 days) on checkout promise dates for high-risk corridors will immediately restore OTIF rates above 90% without adding carrier freight expense.

### 3.2. Structural Fulfillment Flaws vs. Seasonal Spikes
- **Analysis**: Time-based decomposition reveals that monthly delay rates remain virtually flat between **54.0% and 54.8%** throughout the entire calendar year. Hour-of-day order intake and day-of-week dispatch likewise show minimal variance (~54%–55%).
- **Supply Chain Takeaway**: Delay rates are **systemic and structural**, not the result of holiday surges, flash sales, or warehouse shift timing. The carrier contracts and line-haul routes themselves have unrealistic delivery baselines.

### 3.3. Regional Line-Haul Vulnerabilities
- **Analysis**: Delays are heavily localized in cross-border and complex logistics networks:
  - **Central Africa**: 59.8% late delivery rate
  - **East Africa**: 58.3% late delivery rate
  - **Western Europe**: 56.4% late delivery rate
  - **South Asia**: 55.9% late delivery rate
- **Supply Chain Takeaway**: Cross-border customs clearance and local carrier handoffs require region-specific SLA tiers rather than global uniform delivery standards.

### 3.4. Margin Defense & Unprofitable Fulfillments
- **Analysis**: **18.69% of all orders lose money** (`Order Profit Per Order < 0`).
- **PM Takeaway**: Fulfillment operations are actively subsidizing unprofitable shipments. An automated order gate must be established at cart checkout to prevent shipping discounts or loss-making fulfillment on low-value items.

---

## 4. Machine Learning Product: Pre-Dispatch SLA Risk Engine

To transition from retrospective reporting to real-time risk mitigation, we designed a predictive classifier embedded into the fulfillment workflow.

```text
┌─────────────────┐      ┌─────────────────────────┐      ┌──────────────────────┐
│  Customer Cart  │ ───► │ Predictive Risk Engine  │ ───► │ Automated Mitigation │
│  Checkout Event │      │ (Random Forest + SMOTE) │      │   Action Triggered   │
└─────────────────┘      └─────────────────────────┘      └──────────────────────┘
                                  │                                  │
                                  ▼                                  ▼
                         Scored Risk: > 0.50             • Upgrade Carrier Tier
                         Precision  : 78%                • Re-route to Local Hub
                         Recall     : 75%                • Extend Checkout EDD (+2d)
```

### Feature Architecture
The model relies exclusively on **pre-fulfillment data** known at the time of purchase:
- **Order Details**: Transaction Type, Scheduled Delivery Window, Product Category, Department
- **Customer & Destination**: Customer Segment, Destination World Region, Shipping Mode
- **Temporal Context**: Order Month, Order Hour
- **Pre-processing**: High-cardinality nominal variables are encoded using robust frequency encoding. Training data is balanced via **SMOTE** (79,182 balanced instances per class).

### Performance Metrics (Holdout Evaluation: 34,553 Orders)
- **Accuracy**: **74%**
- **Precision (Late Delivery Class)**: **0.78** (When the engine flags an order as at-risk, it is correct in 78% of instances).
- **Recall (Late Delivery Class)**: **0.75** (Catches 3 out of every 4 late shipments before dispatch).
- **F1-Score**: **0.77**

---

## 5. Strategic Recommendations & Product Roadmap

### P0 (Immediate): Dynamic Estimated Delivery Date (EDD) Engine
- **Product Initiative**: Replace static checkout delivery promises with dynamic EDD calculation.
- **Implementation**: For destinations in Central/East Africa or orders utilizing Second Class freight, dynamically append a +1.5 day lead time buffer on the Product Detail Page (PDP) and Checkout.
- **Impact**: Eliminates ~70% of customer-facing SLA breaches overnight without increasing logistics costs.

### P1 (Next Quarter): Dynamic Carrier Routing & Expedited Tier Swapping
- **Supply Chain Initiative**: Integrate the ML Risk Engine directly into the Warehouse Management System (WMS).
- **Implementation**: If an order from a high-LTV customer is flagged as high-risk ($p_{\text{late}} > 0.70$), automatically upgrade the 3PL carrier service tier from Standard to First Class / Express before parcel pickup.
- **Impact**: Safeguards high-value accounts and directly defends the **$2.06M in vulnerable profit**.

### P2 (Long-term): Margin Protection Fulfillment Gate
- **Product & Finance Initiative**: Establish an OMS margin validation rule.
- **Implementation**: Block promotional free shipping on orders where product gross margin is insufficient to cover fulfillment overhead, addressing the 18.7% loss-making order cohort.

---

## 6. Architecture of the Automated CLI Pipeline (`run_analysis.py`)

### 6.1. Why Build a CLI Pipeline Instead of Solely Relying on Notebooks?
While Jupyter Notebooks (`.ipynb`) are ideal for iterative experimentation and EDA prototyping, they introduce significant friction in production environments:
- **State Dependency**: Notebook cells can be run out of order, leading to hidden bugs.
- **Automation Incompatibility**: CI/CD pipelines, Airflow DAGs, and Docker containers cannot easily execute interactive notebooks without heavy orchestration wrappers.
- **Output Volatility**: Figures and metrics printed in notebooks are trapped in JSON blobs rather than saved as standalone files for downstream business intelligence dashboards.

The **Automated CLI Pipeline (`run_analysis.py`)** productionizes the complete methodology into a deterministic, headless, one-command script.

```text
========================================================================================
                     AUTOMATED CLI PIPELINE EXECUTION STAGES
========================================================================================
[Stage 1/7] Ingestion & Path Resolution  ──► Auto-detects archive/ paths with fallback
[Stage 2/7] Data Cleaning & Cleansing    ──► Drops 33 PII/redundant cols; filters canceled
[Stage 3/7] Feature Engineering          ──► Computes Processing Time, Delay, Profit Flag
[Stage 4/7] KPI Computation & Export     ──► Calculates OTIF, P90, Margin Risk -> JSON/TXT
[Stage 5/7] Visualization Engine (Agg)   ──► Exports 6 publication-grade 300 DPI PNG charts
[Stage 6/7] Predictive ML Training       ──► Frequency Encoding + SMOTE + Random Forest
[Stage 7/7] Model & Metrics Persistence  ──► Serializes model.joblib + classification_report
========================================================================================
```

### 6.2. Stage-by-Stage Technical Breakdown
1. **Headless Plotting (`matplotlib.use('Agg')`)**:
   - Notebooks rely on inline interactive plotting backends. `run_analysis.py` configures the headless `Agg` backend to generate rasterized, 300-DPI charts directly to disk without requiring an X11 window server or GUI display.
2. **Robust Path Resolution**:
   - Dynamically resolves dataset locations relative to the file's directory (`__file__`), eliminating hardcoded absolute paths (like the Windows paths previously present).
3. **Structured Non-Destructive Outputs (`outputs/`)**:
   - Preserves source datasets in pristine condition.
   - Exports machine-readable JSON metrics (`business_kpis.json`, `classification_report.json`), tabular summaries (`category_bottlenecks.csv`, `delay_distribution.csv`), and text reports (`business_kpis_summary.txt`) for BI ingestion.
4. **Reproducible Machine Learning**:
   - Enforces a deterministic random seed (`random_state=42`), stratified sampling (`stratify=y`), and parallel multi-core training (`n_jobs=-1`), executing the entire 172K-row ML training workflow in under **3 seconds**.
5. **Model Serialization**:
   - Serializes the fitted Random Forest classifier via `joblib.dump()` to `outputs/models/random_forest_model.joblib` for inference serving.

---

## 7. Repository Structure

```text
supply-chain-analysis/
├── README.md                                # Executive documentation & project guide
├── requirements.txt                         # Pinned dependency specifications
├── run_analysis.py                          # Automated CLI pipeline execution script
├── SupplyChainManagementProject.ipynb        # Fully executed Jupyter Notebook with visual outputs
├── archive/                                 # Raw data directory
│   ├── DataCoSupplyChainDataset.csv         # 180,519 order transactions (91.5 MB)
│   ├── DescriptionDataCoSupplyChain.csv     # Field definitions & data dictionary
│   └── tokenized_access_logs.csv            # Web traffic access logs (91.0 MB)
└── outputs/                                 # Exported deliverables & reports
    ├── figures/                             # Generated high-resolution visualization charts
    │   ├── 01_profitability_distribution.png
    │   ├── 02_delay_distribution_and_profit_analysis.png
    │   ├── 03_bottleneck_detection_by_category.png
    │   ├── 04_root_cause_central_africa.png
    │   ├── 05_root_cause_east_africa.png
    │   └── 06_time_based_delay_trends.png
    ├── reports/                             # Calculated KPIs and tabular reports
    │   ├── business_kpis.json
    │   ├── business_kpis_summary.txt
    │   ├── category_bottlenecks.csv
    │   ├── classification_report.json
    │   ├── classification_report.txt
    │   ├── delay_by_day.csv
    │   ├── delay_by_hour.csv
    │   ├── delay_by_month.csv
    │   ├── delay_distribution.csv
    │   ├── profit_metrics_by_delay_day.csv
    │   ├── root_cause_central_africa.csv
    │   └── root_cause_east_africa.csv
    └── models/
        └── README.md                        # Model generation instructions
```

---

## 8. Setup & Execution Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/prathmeshmdeshmane001/supply-chain-analysis.git
cd supply-chain-analysis
```

### Step 2: Set Up Python Environment
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install pinned dependencies
pip install -r requirements.txt
```

### Step 3: Run the Analysis Pipeline (Automated CLI)
```bash
# Execute complete analysis, generate reports, charts, and train ML model (~9 seconds)
python run_analysis.py
```

### Step 4: Launch Interactive Notebook
```bash
# Run Jupyter Notebook interactively
jupyter notebook SupplyChainManagementProject.ipynb
```