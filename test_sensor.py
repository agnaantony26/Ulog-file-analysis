import pandas as pd
import matplotlib.pyplot as plt

# Example data (replace with your actual data)
data = pd.DataFrame({
    'timestamp': [1, 2, 3, 4, 5],
    'gyro_rad[0]': [0.1, 0.2, 0.3, 0.4, 0.5],
    'accelerometer_m_s2[0]': [9.8, 9.8, 9.8, 9.8, 9.8], #Example to show the plot
    'magnetometer_ga[0]':[1,2,3,4,5]
})
print(data.columns)
if all(col in data.columns for col in ['timestamp', 'gyro_rad[0]', 'gyro_rad[1]', 'gyro_rad[2]', 
                                       'accelerometer_m_s2[0]', 'accelerometer_m_s2[1]', 'accelerometer_m_s2[2]', 
                                       'magnetometer_ga[0]', 'magnetometer_ga[1]', 'magnetometer_ga[2]']):
    print("All required columns are present")
    plt.plot(data['timestamp'], data['gyro_rad[0]'], label="Gyro X (rad/s)")
    plt.xlabel("Timestamp")
    plt.ylabel("Gyro X (rad/s)")
    plt.title("Gyro X Data")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print(f"Missing required columns in sensor_combined data: {list(data.columns)}")