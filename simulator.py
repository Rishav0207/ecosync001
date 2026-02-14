# simulator.py
import pandas as pd
import numpy as np

def generate_data():
    zones = 25
    data = {
        "zone": [],
        "soil_moisture": [],
        "water_level": [],
        "aqi": [],
        "temperature": []
    }

    for i in range(zones):
        data["zone"].append(i)
        data["soil_moisture"].append(np.random.randint(20, 80))
        data["water_level"].append(np.random.randint(30, 100))
        data["aqi"].append(np.random.randint(50, 200))
        data["temperature"].append(np.random.randint(20, 40))

    return pd.DataFrame(data)
