import matplotlib.pyplot as plt
import seaborn as sns

# Sensor prioritization data
sensor_prioritization = {
    "sensor_accel": 9,   # High priority for detecting motion and orientation
    "sensor_gyro": 8,    # High priority for rotational velocity
    "sensor_baro": 7,    # Priority for altitude estimation
    "sensor_gps": 10,    # Top priority for navigation and positioning
    "sensor_mag": 6,     # Medium priority for directional data
    "sensor_combined": 8, # High priority as it consolidates multiple sensors
    "sensors_status_imu": 5 # Moderate priority for IMU health
}

# Extract keys and values
sensors = list(sensor_prioritization.keys())
priorities = list(sensor_prioritization.values())

light_blue = '#ADD8E6'

# Plotting the horizontal stacked bar chart
plt.figure(figsize=(10, 6))
plt.barh(sensors, priorities, color=light_blue, edgecolor='black', height=0.6)

# Add labels and title
plt.xlabel("Priority Level (1-10)", fontsize=12)
plt.ylabel("Sensors", fontsize=12)
plt.title("Sensor Data Prioritization", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the values inside the bars
for index, value in enumerate(priorities):
    plt.text(value - 0.5, index, str(value), va='center', ha='center', color='white', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()
