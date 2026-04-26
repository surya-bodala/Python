import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data():
    data = []
    for i in range(15):
        zone_data = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone_data)
    return data[::-1]

def copy_data(data):
    assign = data
    shallow = copy.copy(data)
    deep = copy.deepcopy(data)
    return assign, shallow, deep

def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["history"].append(random.randint(10, 100))
        total = d["metrics"]["traffic"] + d["metrics"]["pollution"] + d["metrics"]["energy"]
        d["risk"] = math.log(total)
    return data

def create_dataframe(data):
    rows = []
    for d in data:
        row = {
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": d["risk"]
        }
        rows.append(row)
    return pd.DataFrame(rows)

def analysis(df):
    values = df[["traffic", "pollution", "energy", "risk"]].values
    mean = np.mean(values, axis=0)
    var = np.var(values, axis=0)
    std = np.std(values, axis=0)

    corr = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            xi = values[:, i]
            xj = values[:, j]
            corr[i][j] = np.sum((xi - np.mean(xi))*(xj - np.mean(xj))) / (len(xi)*np.std(xi)*np.std(xj))

    anomalies = df[df["risk"] > (df["risk"].mean() + df["risk"].std())]

    return mean, var, corr, anomalies

def advanced(df, var):
    risks = df["risk"].values
    high = risks > np.mean(risks)

    clusters = []
    temp = []
    for i in range(len(high)):
        if high[i]:
            temp.append(df["zone"][i])
        else:
            if temp:
                clusters.append(temp)
                temp = []
    if temp:
        clusters.append(temp)

    stability = 1 / np.mean(var)
    return max(risks), min(risks), stability, clusters

def decision(stability):
    if stability > 1:
        return "System Stable"
    elif stability > 0.5:
        return "Moderate Risk"
    elif stability > 0.2:
        return "High Corruption Risk"
    else:
        return "Critical Failure"

data = generate_data()
assign, shallow, deep = copy_data(data)

original_before = copy.deepcopy(data)

mutated = mutate_data(shallow)

df = create_dataframe(mutated)

mean, var, corr, anomalies = analysis(df)

max_risk, min_risk, stability, clusters = advanced(df, var)

status = decision(stability)

print(df)
print("\nOriginal vs After Mutation\n")
print(original_before[0])
print(mutated[0])
print("\nAnomalies:\n", anomalies)
print("\nTuple:", (max_risk, min_risk, stability))
print("\nClusters:", clusters)
print("\nFinal Decision:", status)
