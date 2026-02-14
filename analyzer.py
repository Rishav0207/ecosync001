# analyzer.py
def analyze(df):
    alerts = []

    for _, row in df.iterrows():
        if row["soil_moisture"] < 30:
            alerts.append(f"Zone {row['zone']}: Dry soil")
        if row["aqi"] > 150:
            alerts.append(f"Zone {row['zone']}: High pollution")
        if row["water_level"] < 40:
            alerts.append(f"Zone {row['zone']}: Low water level")

    return alerts
