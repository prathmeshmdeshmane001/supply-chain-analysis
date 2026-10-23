# Share Copy Variants — End to End Supply Chain Analysis

## Twitter / X
We audited 172,765 orders and found something remarkable: paying extra for First Class shipping guarantees a 100% late delivery rate.

While executive dashboards celebrated record revenue, the fleet was bleeding $2.06M in delayed delivery churn.

We built an end-to-end ML pipeline + Streamlit console to predict dispatch failure at checkout and protect margins in real time.

## LinkedIn
In supply chain management, what you don't measure quietly erodes your margins.

In our audit of 172,765 orders from DataCo Global:
• Fleet-wide late delivery rate: 54.71% (94,528 orders delayed)
• Same Day Delivery: 0.0% late (flawless)
• First Class Priority: 100.0% late (complete SLA inversion)
• Margin exposure: $2,055,765 in customer churn risk

Standard BI dashboards focused purely on gross revenue and completely missed the delay penalty. 

To solve this, I designed and deployed an end-to-end machine learning solution:
1. Imbalance remediation using SMOTE (balancing 94K late vs 78K on-time orders).
2. Random Forest classifier achieving 74% accuracy and 78% precision.
3. Automated CLI pipeline & interactive Streamlit KPI dashboard for proactive rerouting.

Available now on GitHub.

## Discord / Developer Communities
Just published an End-to-End Supply Chain ML project. Audited 172K logistics records and found an absurd SLA inversion: 100% of First Class shipments were delayed, causing $2.06M in margin bleed. Built a Random Forest + SMOTE pipeline with real-time CLI inference and a Streamlit dashboard to predict and mitigate delays before dispatch.
