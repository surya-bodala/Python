🧠 Smart Data Replication & Risk Analytics System
📌 Overview

This project combines:

🔁 Data copying techniques (Assignment, Shallow, Deep)
📊 Numerical analysis using NumPy & Pandas
🧠 Risk modeling & anomaly detection

It simulates a system that monitors multiple zones, mutates data, and evaluates stability, corruption risk, and anomalies.

⚙️ Features
📦 Complex nested data generation
🔁 Copy comparison (Assignment vs Shallow vs Deep)
✏️ Data mutation with logarithmic risk calculation
📊 Statistical analysis (mean, variance, std deviation)
🔗 Manual correlation matrix computation
🚨 Anomaly detection
🧩 Cluster identification
🧠 Stability-based decision system
🗂️ Data Structure

Each zone contains:

zone → Zone ID
metrics →
traffic 🚗
pollution 🌫️
energy ⚡
history → Past values list
risk → Computed later

Example:

{
  "zone": 1,
  "metrics": {
    "traffic": 120,
    "pollution": 80,
    "energy": 90
  },
  "history": [20, 35, 50, 60, 75]
}
🔁 Copy Mechanisms
Assignment Copy
assign = data
Same reference
⚠️ Changes fully affect original
Shallow Copy
shallow = copy.copy(data)
Outer copy only
Inner structures shared
⚠️ Partial corruption
Deep Copy
deep = copy.deepcopy(data)
Fully independent
✅ No corruption
✏️ Mutation Logic

Each zone is modified:

Traffic increased by +10
New history value appended
Risk calculated using logarithm:
risk = log(traffic + pollution + energy)
📊 Data Analysis
Statistical Measures
Mean
Variance
Standard Deviation
Correlation Matrix

Manually computed using:

corr(x,y) = Σ[(xi - mean(x)) * (yi - mean(y))] / (n * std(x) * std(y))
🚨 Anomaly Detection

Zones where:

risk > mean(risk) + std(risk)

→ Marked as anomalies

🧩 Advanced Analysis
Clusters
Consecutive zones with above-average risk
Stability Score
stability = 1 / mean(variance)
🚦 Decision System

Based on stability:

Stability Value	Decision
> 1	System Stable ✅
> 0.5	Moderate Risk ⚠️
> 0.2	High Corruption Risk 🚨
≤ 0.2	Critical Failure 🔥
📊 Output

The program prints:

DataFrame of all zones
Original vs mutated data comparison
Detected anomalies
Risk tuple:
(max_risk, min_risk, stability)
Clusters
Final system decision
🧑‍💻 Requirements
pip install numpy pandas
▶️ How to Run
python your_script_name.py
🧪 Key Insights
Shallow copy causes hidden data corruption
Deep copy preserves original dataset
Log-based risk helps normalize large values
Stability inversely depends on variance
⚠️ Concept: Data Corruption

Data corruption occurs when:

Changes in copied data unintentionally modify the original due to shared references.

📎 Notes
Data is randomized each run
Reverse ordering adds variation in clustering
Manual correlation helps understand underlying math
