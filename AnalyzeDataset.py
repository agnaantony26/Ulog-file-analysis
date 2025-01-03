from pyulog import ULog
import pandas as pd
import matplotlib.pyplot as plt

ulog_file_path = '/Users/agna/Downloads/log_0_2024-11-8-14-14-58.ulg'
ulog = ULog(ulog_file_path)

# Extract datasets
datasets = {
    "mission_result": ulog.get_dataset('mission_result'),
    "position_setpoint_triplet": ulog.get_dataset('position_setpoint_triplet'),
    "vehicle_status": ulog.get_dataset('vehicle_status'),
    "vehicle_local_position": ulog.get_dataset('vehicle_local_position'),
    "vehicle_global_position": ulog.get_dataset('vehicle_global_position'),
}

# Analyze Mission Result
mission_result_data = pd.DataFrame(datasets['mission_result'].data)
print("Mission Result Summary:")
print(mission_result_data.describe())

# Plot Mission Pathway 
import numpy as np

if 'x' in datasets['vehicle_local_position'].data.keys() and 'y' in datasets['vehicle_local_position'].data.keys():
    # Convert the data to a pandas DataFrame
    local_position_data = pd.DataFrame(datasets['vehicle_local_position'].data)
    
    # Ensure 'x' and 'y' are converted to 1D numpy arrays
    x_data = np.array(local_position_data['x'])
    y_data = np.array(local_position_data['y'])

    # Plot Mission Pathway
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, label="Mission Pathway")
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Drone Mission Pathway')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Keys 'x' and 'y' are not found in the dataset.")

# Extract Vehicle Status
vehicle_status_data = pd.DataFrame(datasets['vehicle_status'].data)
mission_modes = vehicle_status_data['nav_state'].unique()
print(f"Vehicle Navigation States: {mission_modes}")
