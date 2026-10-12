# Supply Chain Analysis & Late Delivery Prediction

An end-to-end exploratory data analysis, root-cause bottleneck detection, and machine learning pipeline for predicting supply chain late delivery risk and assessing delivery impact on profitability.

---

## 1. Project Structure

```text
Supply Chain Analysis/
├── README.md                                # Project documentation
├── requirements.txt                         # Complete pinned Python environment dependencies
├── run_analysis.py                          # Automated CLI execution script for the analysis & ML pipeline
├── SupplyChainManagementProject.ipynb        # Primary analysis Jupyter notebook (all cells executed)
├── archive/                                 # Raw data directory
│   ├── DataCoSupplyChainDataset.csv         # Main dataset (180,519 records, 53 features)
│   ├── DescriptionDataCoSupplyChain.csv     # Data dictionary (field descriptions)
│   └── tokenized_access_logs.csv            # Web traffic / server access logs (469,978 records)
└── outputs/                                 # Generated analytical artifacts
    ├── figures/                             # Generated high-resolution visualization charts
    │   ├── 01_profitability_distribution.png
    │   ├── 02_delay_distribution_and_profit_analysis.png
    │   ├── 03_bottleneck_detection_by_category.png
    │   ├── 04_root_cause_central_africa.png
    │   ├── 05_root_cause_east_africa.png
    │   └── 06_time_based_delay_trends.png
    ├── reports/                             # Calculated KPIs, summaries, and tabular metrics
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
    └── models/                              # Trained machine learning model artifacts
        └── random_forest_model.joblib
```

---

## 2. Environment Setup

The project uses Python (>=3.11/3.12) with a localized virtual environment:

```bash
# 1. Create a virtual environment
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 3. How to Run

### Option A: Command-Line Pipeline Execution (Recommended)
To run the complete data processing, KPI evaluation, chart generation, and model training end-to-end:

```bash
.venv/bin/python run_analysis.py
```

### Option B: Interactive Jupyter Notebook
To inspect or run the notebook interactively:

```bash
.venv/bin/jupyter notebook SupplyChainManagementProject.ipynb
```
Or execute headless:
```bash
.venv/bin/python -c "import nbformat; from nbclient import NotebookClient; nb = nbformat.read('SupplyChainManagementProject.ipynb', as_version=4); NotebookClient(nb, timeout=600).execute(); nbformat.write(nb, open('SupplyChainManagementProject.ipynb', 'w'))"
```

---

## 4. Analytical Highlights & Results

- **Dataset Scope**:
  - Total raw records: 180,519
  - Cleaned records (excluding canceled orders): 172,765
- **Order Performance & Delivery KPIs**:
  - **Total Orders Evaluated**: 172,765
  - **Late Deliveries**: 94,523 orders
  - **Late Delivery Rate**: 54.71%
  - **On-time Delivery Rate**: 45.29%
  - **90th Percentile Delay**: 3.0 days
- **Financial Impact**:
  - **Total Profit**: $7,514,813.81 (~$7.5M)
  - **Total Order Value at Risk from Delayed Deliveries**: $2,055,765.16 (~$2.1M)
  - **Order Profitability Split**: 80.66% Profit, 18.69% Loss, 0.65% Break-even
- **Predictive Modeling (Random Forest + SMOTE)**:
  - **Target**: `Late_delivery_risk` (Binary: 0 = On Time, 1 = Late)
  - **Class Distribution**: 98,977 Late vs 73,788 On Time
  - **Balancing**: SMOTE applied on training set (79,182 samples per class)
  - **Test Performance (34,553 holdout orders)**:
    - **Accuracy**: 74%
    - **Precision**: 0.78
    - **Recall**: 0.75
    - **F1-Score**: 0.77 (Class 1) / 0.70 (Class 0)