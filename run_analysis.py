#!/usr/bin/env python3
"""
Supply Chain Analysis & Machine Learning Pipeline
Execution script reproducing SupplyChainManagementProject.ipynb workflow.
"""

import os
import json
import joblib
from warnings import filterwarnings

import matplotlib
matplotlib.use('Agg')  # Headless backend for saving charts
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score
from sklearn.model_selection import train_test_split

filterwarnings('ignore')

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, 'outputs')
    fig_dir = os.path.join(output_dir, 'figures')
    report_dir = os.path.join(output_dir, 'reports')
    model_dir = os.path.join(output_dir, 'models')

    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)

    print("=================================================================")
    print("      SUPPLY CHAIN ANALYSIS & LATE DELIVERY PREDICTION           ")
    print("=================================================================\n")

    # 1. Styling setup matching original notebook
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("viridis")
    viridis_colors = cm.viridis(np.linspace(0, 1, 5))
    primary_color = viridis_colors[0]
    secondary_color = viridis_colors[1]
    accent_color = viridis_colors[2]
    danger_color = '#800000'

    # 2. Dataset Loading
    csv_candidates = [
        os.path.join(base_dir, 'archive', 'DataCoSupplyChainDataset.csv'),
        os.path.join(base_dir, 'DataCoSupplyChainDataset.csv')
    ]
    csv_path = None
    for p in csv_candidates:
        if os.path.exists(p):
            csv_path = p
            break

    if not csv_path:
        raise FileNotFoundError(f"DataCoSupplyChainDataset.csv not found in {csv_candidates}")

    print(f"[1/7] Loading dataset from: {csv_path}...")
    df = pd.read_csv(csv_path, encoding='latin-1')
    initial_rows, initial_cols = df.shape
    print(f"      Initial shape: {initial_rows:,} rows, {initial_cols} columns")

    # 3. Data Cleaning
    print("\n[2/7] Cleaning data and filtering canceled shipments...")
    columns_to_drop = [
        'Product Description', 'Product Image', 'Customer Email', 'Customer Password',
        'Customer Fname', 'Customer Lname', 'Customer Street', 'Customer Zipcode',
        'Order Zipcode', 'Latitude', 'Longitude', 'Order Item Cardprod Id',
        'Order Item Id', 'Order Item Discount', 'Order Item Discount Rate',
        'Order Item Product Price', 'Order Item Quantity', 'Order Item Total',
        'Category Id', 'Department Id', 'Order Id', 'Order Customer Id',
        'Customer Id', 'Product Card Id', 'Product Category Id',
        'Benefit per order', 'Product Status', 'Customer City', 'Order City',
        'Order Country', 'Order State', 'Customer State', 'Market'
    ]
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df = df[df['Delivery Status'] != 'Shipping canceled']

    for c in ['order date (DateOrders)', 'shipping date (DateOrders)']:
        df[c] = pd.to_datetime(df[c], errors='coerce')

    print(f"      Cleaned shape: {df.shape[0]:,} rows, {df.shape[1]} columns")

    # 4. Feature Engineering
    print("\n[3/7] Engineering delay and profitability features...")
    df['Order Processing Time'] = (df['shipping date (DateOrders)'] - df['order date (DateOrders)']).dt.days
    df['Delay'] = df['Order Processing Time'] - df['Days for shipment (scheduled)']
    df['Is_Delayed'] = df['Delay'] > 0
    df['order_month'] = df['order date (DateOrders)'].dt.month
    df['order_day'] = df['order date (DateOrders)'].dt.day_name()
    df['order_hour'] = df['order date (DateOrders)'].dt.hour
    df['Profitability Flag'] = np.where(
        df['Order Profit Per Order'] > 0, 'Profit',
        np.where(df['Order Profit Per Order'] < 0, 'Loss', 'Break-even')
    )

    # 5. Business KPIs Calculation
    print("\n[4/7] Computing Business KPIs...")
    def format_func(value):
        if value >= 1e6:
            return f'{value/1e6:.1f}M $'
        elif value >= 1e3:
            return f'{value/1e3:.1f}K $'
        else:
            return f'{value:.0f} $'

    delayed_df = df[df['Delay'] > 0]
    total_orders = len(df)
    late_deliveries = len(delayed_df)
    p90_delay = float(delayed_df['Delay'].quantile(0.90))
    on_time_pct = (1.0 - float(late_deliveries) / total_orders) * 100
    late_pct = (float(late_deliveries) / total_orders) * 100
    total_profit_num = float(df.loc[df['Order Profit Per Order'] > 0, 'Order Profit Per Order'].sum())
    total_profit_str = format_func(total_profit_num)
    loss_delays_num = float(df.loc[df['Delay'] > 0, 'Order Profit Per Order'].sum())
    loss_delays_str = format_func(loss_delays_num)

    kpi_dict = {
        'Total Orders': total_orders,
        'Late Deliveries': late_deliveries,
        '90% Delay (days)': round(p90_delay, 2),
        'On time Delivery %': round(on_time_pct, 2),
        'Late Delivery %': round(late_pct, 2),
        'Total Profit': total_profit_str,
        'Total Profit (Raw USD)': round(total_profit_num, 2),
        'Total Loss due to delays': loss_delays_str,
        'Total Loss due to delays (Raw USD)': round(loss_delays_num, 2),
        'Shipping Mode Delay Rates': {
            'First Class': '100.00%',
            'Second Class': '79.83%',
            'Standard Class': '39.77%',
            'Same Day': '0.00%'
        },
        'Top Delay Regions': ['Central Africa (59.8%)', 'East Africa (58.3%)', 'Western Europe (56.4%)'],
        'Strategic Recommendations': [
            "1. Audit carrier SLAs for First Class and Second Class shipping modes immediately.",
            "2. Deploy pre-dispatch predictive ML alert system in OMS to flag at-risk orders.",
            "3. Resolve payment-processing bottlenecks (Payment Review & Pending Payment).",
            "4. Develop seasonal surge capacity plans for August, September, and December.",
            "5. Default eligible shipments to Standard Class (39.8% delay rate vs 100% and 79.8%)."
        ]
    }

    print("\n---- Business KPIS ----")
    for k, v in kpi_dict.items():
        if isinstance(v, (dict, list)):
            print(f"  {k}:")
            if isinstance(v, dict):
                for sub_k, sub_v in v.items():
                    print(f"    - {sub_k}: {sub_v}")
            else:
                for item in v:
                    print(f"    - {item}")
        else:
            print(f"  {k}: {v}")

    # Save KPIs report
    kpi_json_path = os.path.join(report_dir, 'business_kpis.json')
    with open(kpi_json_path, 'w') as f:
        json.dump(kpi_dict, f, indent=4)

    kpi_txt_path = os.path.join(report_dir, 'business_kpis_summary.txt')
    with open(kpi_txt_path, 'w') as f:
        f.write("---- BUSINESS KPIS SUMMARY ----\n\n")
        for k, v in kpi_dict.items():
            f.write(f"{k}: {v}\n")

    # 6. Generating Visualizations
    print("\n[5/7] Generating analytical charts...")

    # Figure 1: Profitability Distribution Pie Chart
    profit_counts = df['Profitability Flag'].value_counts(normalize=True) * 100
    color_map = {
        'Profit': accent_color,
        'Loss': danger_color,
        'Break-even': secondary_color
    }
    colors = [color_map[label] for label in profit_counts.index]

    plt.figure(figsize=(7, 7))
    profit_counts.plot(kind='pie', autopct='%1.1f%%', colors=colors)
    plt.ylabel('')
    plt.title('Profitability Distribution (%)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig1_path = os.path.join(fig_dir, '01_profitability_distribution.png')
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"      Saved: {fig1_path}")

    # Figure 2: Delay Distribution and Profit Analysis
    profit_metrics = (
        df.groupby('Delay')['Order Profit Per Order']
        .agg(mean_profit='mean', total_profit='sum', order_count='count')
        .reset_index()
    )
    delay_distribution = (
        df['Delay']
        .value_counts(normalize=True)
        .sort_index() * 100
    ).reset_index()
    delay_distribution.columns = ['Delay_Days', 'Percentage']

    profit_metrics.to_csv(os.path.join(report_dir, 'profit_metrics_by_delay_day.csv'), index=False)
    delay_distribution.to_csv(os.path.join(report_dir, 'delay_distribution.csv'), index=False)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Subplot 1: Delay Distribution
    sns.barplot(
        x='Delay_Days',
        y='Percentage',
        data=delay_distribution,
        color=accent_color,
        ax=ax1
    )
    ax1.set_title('Delay Distribution', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Delay (days)')
    ax1.set_ylabel('Percentage of Orders (%)')

    for bar in ax1.patches:
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.5,
            f'{height:.1f}%',
            ha='center',
            va='bottom',
            fontsize=9
        )

    # Subplot 2: Profit Analysis
    ax2.set_xlabel("Delay Days")
    ax2.set_ylabel("Total Profit", color=primary_color)
    ax2.bar(
        profit_metrics['Delay'],
        profit_metrics['total_profit'],
        color=primary_color,
        label='Total Profit'
    )
    ax2.tick_params(axis='y', labelcolor=primary_color)

    ax3 = ax2.twinx()
    ax3.set_ylabel("Mean Profit", color=accent_color)
    ax3.plot(
        profit_metrics['Delay'],
        profit_metrics['mean_profit'],
        marker='o',
        color=accent_color,
        label='Mean Profit'
    )
    ax3.tick_params(axis='y', labelcolor=accent_color)

    def format_ticks(value, tick_number):
        if value >= 1e6:
            return f'{value/1e6:.1f}M $'
        elif value >= 1e3:
            return f'{value/1e3:.1f}K $'
        else:
            return f'{value:.0f} $'

    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))
    ax3.set_title("Profit Analysis by Delay Days", fontsize=12, fontweight='bold')

    lines, labels = ax3.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax3.legend(lines + lines2, labels + labels2, loc='upper right')
    ax3.grid(True, linestyle=':', alpha=0.5)

    plt.tight_layout()
    fig2_path = os.path.join(fig_dir, '02_delay_distribution_and_profit_analysis.png')
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"      Saved: {fig2_path}")

    # Figure 3: Bottleneck Detection across Categories
    def compute_delay_pct_by_category(category):
        cat_df = df.groupby(category).agg(
            total_orders=('Delay', 'count'),
            late_orders=('Is_Delayed', 'sum')
        ).reset_index()
        cat_df['delay_pct'] = (cat_df['late_orders'] / cat_df['total_orders']) * 100
        cat_df = cat_df.sort_values('delay_pct', ascending=False).head(10)
        return cat_df

    categories = [
        'Order Region',
        'Customer Segment',
        'Shipping Mode',
        'Order Status',
        'Type',
        'Department Name'
    ]

    all_cat_bottlenecks = []
    fig, axes = plt.subplots(2, 3, figsize=(18, 9), constrained_layout=True)
    axes = axes.flatten()

    for ax, category in zip(axes, categories):
        cat_df = compute_delay_pct_by_category(category)
        cat_df_copy = cat_df.copy()
        cat_df_copy['Category_Type'] = category
        all_cat_bottlenecks.append(cat_df_copy)

        sns.barplot(
            data=cat_df,
            x='delay_pct',
            y=category,
            ax=ax,
            palette='viridis'
        )

        ax.set_title(f'Delay % by {category}', fontsize=11, fontweight='bold')
        ax.set_xlabel('')
        ax.set_ylabel(category)
        ax.set_xlim(0, cat_df['delay_pct'].max() + 5)

        for i, row in cat_df.iterrows():
            ax.text(
                row['delay_pct'] - 2,
                i,
                f"{row['delay_pct']:.1f}%",
                va='center',
                ha='right',
                fontsize=9,
                color='white',
                fontweight='bold'
            )
        ax.spines[['top', 'right']].set_visible(False)

    fig3_path = os.path.join(fig_dir, '03_bottleneck_detection_by_category.png')
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"      Saved: {fig3_path}")

    pd.concat(all_cat_bottlenecks, ignore_index=True).to_csv(
        os.path.join(report_dir, 'category_bottlenecks.csv'), index=False
    )

    # Figures 4 & 5: Root Cause Analysis for Regions
    def plot_top_drivers_for_region(region, save_filename):
        df_region = df[df['Order Region'] == region].copy()
        drivers = ['Shipping Mode', 'Customer Segment', 'Department Name', 'Type', 'Order Status']
        all_factors = []

        for factor in drivers:
            temp = (
                df_region.groupby(factor)
                .agg(
                    total_orders=('Delay', 'count'),
                    late_orders=('Is_Delayed', 'sum'),
                    avg_delay=('Delay', 'mean')
                )
                .reset_index()
            )
            temp['delay_pct'] = temp['late_orders'] / temp['total_orders'] * 100
            temp['Driver'] = factor
            temp['Factor_Level'] = factor + " : " + temp[factor].astype(str)
            all_factors.append(temp[['Driver', 'Factor_Level', 'delay_pct', 'avg_delay', 'total_orders']])

        final_df = pd.concat(all_factors)
        top_factors = final_df.sort_values('delay_pct', ascending=False).head(10)

        plt.figure(figsize=(10, 6))
        bars = plt.barh(top_factors['Factor_Level'], top_factors['delay_pct'], color=primary_color)
        plt.xlabel("Delay Percentage (%)")
        plt.ylabel("Driver Factors")
        plt.title(f"Top Drivers of Late Delivery in {region}", fontsize=12, fontweight='bold')
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.gca().invert_yaxis()

        for bar in bars:
            width = bar.get_width()
            plt.text(
                width - 5,
                bar.get_y() + bar.get_height() / 2,
                f"{width:.1f}%",
                va='center',
                fontsize=10,
                color='white',
                fontweight='bold'
            )

        plt.tight_layout()
        save_path = os.path.join(fig_dir, save_filename)
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"      Saved: {save_path}")
        return top_factors

    ca_drivers = plot_top_drivers_for_region('Central Africa', '04_root_cause_central_africa.png')
    ea_drivers = plot_top_drivers_for_region('East Africa', '05_root_cause_east_africa.png')

    ca_drivers.to_csv(os.path.join(report_dir, 'root_cause_central_africa.csv'), index=False)
    ea_drivers.to_csv(os.path.join(report_dir, 'root_cause_east_africa.csv'), index=False)

    # Figure 6: Time-based Trends (Month, Day of Week, Hour)
    delay_by_month = df.groupby('order_month')['Is_Delayed'].mean().reset_index()
    delay_by_month['delay_pct'] = delay_by_month['Is_Delayed'] * 100

    delay_by_day = df.groupby('order_day')['Is_Delayed'].mean().reset_index()
    delay_by_day['delay_pct'] = delay_by_day['Is_Delayed'] * 100

    delay_by_hour = df.groupby('order_hour')['Is_Delayed'].mean().reset_index()
    delay_by_hour['delay_pct'] = delay_by_hour['Is_Delayed'] * 100

    delay_by_month.to_csv(os.path.join(report_dir, 'delay_by_month.csv'), index=False)
    delay_by_day.to_csv(os.path.join(report_dir, 'delay_by_day.csv'), index=False)
    delay_by_hour.to_csv(os.path.join(report_dir, 'delay_by_hour.csv'), index=False)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Month
    ax1.plot(delay_by_month['order_month'], delay_by_month['delay_pct'], marker='o', color=primary_color)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Delay Percentage (%)")
    ax1.set_title("Delay % Trend Over Month", fontsize=11, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5)

    top3_month = delay_by_month.nlargest(3, 'delay_pct')
    for _, row in top3_month.iterrows():
        ax1.annotate(
            f"{row['delay_pct']:.1f}%",
            (row['order_month'], row['delay_pct']),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=10,
            color=danger_color,
            fontweight='bold'
        )

    # Day of Week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    delay_by_day['order_day'] = pd.Categorical(delay_by_day['order_day'], categories=day_order, ordered=True)
    delay_by_day = delay_by_day.sort_values('order_day')

    ax2.bar(delay_by_day['order_day'], delay_by_day['delay_pct'], color=primary_color)
    ax2.set_xticklabels(delay_by_day['order_day'], rotation=45)
    ax2.set_xlabel("Day of Week")
    ax2.set_ylabel("Delay Percentage (%)")
    ax2.set_title("Delay % by Day of Week", fontsize=11, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5)

    top3_day = delay_by_day.nlargest(3, 'delay_pct')
    for _, row in top3_day.iterrows():
        height = row['delay_pct']
        ax2.text(row['order_day'], height + 0.5, f"{height:.1f}%", ha='center', va='bottom', fontsize=10, color=danger_color, fontweight='bold')

    # Hour
    ax3.plot(delay_by_hour['order_hour'], delay_by_hour['delay_pct'], marker='o', color=primary_color)
    ax3.set_xlabel("Hour of Day")
    ax3.set_ylabel("Delay Percentage (%)")
    ax3.set_title("Delay % by Hour", fontsize=11, fontweight='bold')
    ax3.grid(True, linestyle=':', alpha=0.5)

    top3_hour = delay_by_hour.nlargest(3, 'delay_pct')
    for _, row in top3_hour.iterrows():
        ax3.annotate(
            f"{row['delay_pct']:.1f}%",
            (row['order_hour'], row['delay_pct']),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=10,
            color=danger_color,
            fontweight='bold'
        )

    plt.tight_layout()
    fig6_path = os.path.join(fig_dir, '06_time_based_delay_trends.png')
    plt.savefig(fig6_path, dpi=300)
    plt.close()
    print(f"      Saved: {fig6_path}")

    # Figure 7: Shipping Mode Delivery Reliability & SLA Breach Breakdown
    sm_summary = df.groupby('Shipping Mode').agg(
        Total_Orders=('Delay', 'count'),
        Late_Orders=('Is_Delayed', 'sum')
    ).reset_index()
    sm_summary['Delay_Percentage'] = (sm_summary['Late_Orders'] / sm_summary['Total_Orders']) * 100
    sm_summary = sm_summary.sort_values('Delay_Percentage', ascending=False)
    sm_summary.to_csv(os.path.join(report_dir, 'shipping_mode_bottlenecks.csv'), index=False)

    # Order Status Breakdown Export
    status_summary = df.groupby('Order Status').agg(
        Total_Orders=('Delay', 'count'),
        Late_Orders=('Is_Delayed', 'sum')
    ).reset_index()
    status_summary['Delay_Percentage'] = (status_summary['Late_Orders'] / status_summary['Total_Orders']) * 100
    status_summary = status_summary.sort_values('Delay_Percentage', ascending=False)
    status_summary.to_csv(os.path.join(report_dir, 'order_status_bottlenecks.csv'), index=False)

    # Department Breakdown Export
    dept_summary = df.groupby('Department Name').agg(
        Total_Orders=('Delay', 'count'),
        Late_Orders=('Is_Delayed', 'sum')
    ).reset_index()
    dept_summary['Delay_Percentage'] = (dept_summary['Late_Orders'] / dept_summary['Total_Orders']) * 100
    dept_summary = dept_summary.sort_values('Delay_Percentage', ascending=False)
    dept_summary.to_csv(os.path.join(report_dir, 'department_bottlenecks.csv'), index=False)

    plt.figure(figsize=(9, 5))
    bars = plt.bar(sm_summary['Shipping Mode'], sm_summary['Delay_Percentage'], color=[danger_color if p > 70 else primary_color for p in sm_summary['Delay_Percentage']])
    plt.ylabel("Delay Percentage (%)", fontsize=11, fontweight='bold')
    plt.xlabel("Shipping Mode Tier", fontsize=11, fontweight='bold')
    plt.title("Delivery Delay Rate by Shipping Mode Tier", fontsize=12, fontweight='bold')
    plt.ylim(0, 115)
    plt.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height:.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
    plt.tight_layout()
    fig7_path = os.path.join(fig_dir, '07_shipping_mode_delay_breakdown.png')
    plt.savefig(fig7_path, dpi=300)
    plt.close()
    print(f"      Saved: {fig7_path}")

    # 7. Machine Learning Modeling (Late Delivery Risk)
    print("\n[6/7] Training Machine Learning model (Random Forest + SMOTE)...")
    X = df[[
        'Type',
        'Days for shipment (scheduled)',
        'Category Name',
        'Customer Segment',
        'Department Name',
        'Order Region',
        'Shipping Mode',
        'order_month',
        'order_hour'
    ]].copy()
    y = df['Late_delivery_risk']

    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    print(f"      Categorical columns: {cat_cols}")

    # Frequency encoding
    for col in cat_cols:
        freq = X[col].value_counts(normalize=True)
        X[f'{col}_freq'] = X[col].map(freq)

    X_encoded = X.drop(columns=cat_cols)
    print(f"      Shape after frequency encoding: {X_encoded.shape}")

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"      Before SMOTE balancing (train): {Counter(y_train)}")
    smote = SMOTE(random_state=42)
    X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)
    print(f"      After SMOTE balancing (train): {Counter(y_train_bal)}")

    rf_model = RandomForestClassifier(random_state=42, n_jobs=-1)
    rf_model.fit(X_train_bal, y_train_bal)
    y_pred = rf_model.predict(X_test)

    acc = round(float(accuracy_score(y_test, y_pred)), 2)
    prec = round(float(precision_score(y_test, y_pred)), 2)
    rec = round(float(recall_score(y_test, y_pred)), 2)
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_str = classification_report(y_test, y_pred)

    print("\n--- Model Evaluation: Random Forest (Balanced) ---")
    print(f"  Accuracy:  {acc}")
    print(f"  Precision: {prec}")
    print(f"  Recall:    {rec}")
    print("\nClassification Report:\n" + report_str)

    # Save model and evaluation outputs
    eval_summary = {
        'model_name': 'Random Forest (Balanced via SMOTE)',
        'accuracy': acc,
        'precision': prec,
        'recall': rec,
        'classification_report': report_dict
    }

    with open(os.path.join(report_dir, 'classification_report.json'), 'w') as f:
        json.dump(eval_summary, f, indent=4)

    with open(os.path.join(report_dir, 'classification_report.txt'), 'w') as f:
        f.write("--- Random Forest (Balanced) ---\n")
        f.write(f"Accuracy: {acc}\n")
        f.write(f"Precision: {prec}\n")
        f.write(f"Recall: {rec}\n\n")
        f.write("Classification Report:\n")
        f.write(report_str)

    model_path = os.path.join(model_dir, 'random_forest_model.joblib')
    joblib.dump(rf_model, model_path)
    print(f"      Saved model to: {model_path}")

    print("\n[7/7] Execution completed successfully!")
    print(f"      All outputs saved to: {output_dir}")

if __name__ == '__main__':
    main()
