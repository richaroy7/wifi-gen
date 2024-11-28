import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Parameters
num_records = 1000
subcarriers = 56  # For a 20 MHz WiFi channel

# Generate random timestamps
start_time = datetime.now()
timestamps = [start_time + timedelta(seconds=i) for i in range(num_records)]

# Generate data
data = []
for i in range(num_records):
    person_present = random.choice([0, 1])  # 0: Absent, 1: Present
    rssi = random.randint(-90, -30) + (5 if person_present else 0)  # Slight signal boost when present
    csi = [(round(random.uniform(0.1, 1.0), 3) + (0.2 if person_present else 0),
            random.randint(0, 360)) for _ in range(subcarriers)]
    
    record = {
        "Timestamp": timestamps[i].strftime("%Y-%m-%d %H:%M:%S"),
        "Device_ID": f"Device_{random.randint(1, 10)}",
        "RSSI": rssi,
        "SSID": random.choice(["Home_Network", "Cafe_WiFi", "Office_Network"]),
        "Frequency (MHz)": random.choice([2412, 2437, 2462]),
        "Channel": random.choice([1, 6, 11]),
        "Location": (round(random.uniform(23.0, 24.0), 4), round(random.uniform(45.0, 46.0), 4)),
        "CSI": csi,
        "Person_Present": person_present  # Label
    }
    data.append(record)

# Convert to a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_wifi_data_with_labels.csv", index=False)
print("Synthetic WiFi data with labels generated and saved to 'synthetic_wifi_data_with_labels.csv'")
