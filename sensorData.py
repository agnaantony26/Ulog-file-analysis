from pyulog import ULog
import pandas as pd
import matplotlib.pyplot as plt

# Load ULog file
ulog_file_path = "/Users/agna/Downloads/log_0_2024-11-8-14-14-58.ulg"
ulog = ULog(ulog_file_path)

# Explicitly mentioned sensors
explicit_sensors = [
    "sensor_accel",
    "sensor_baro",
    "sensor_combined",
    "sensor_gps",
    "sensor_gyro",
    "sensor_mag",
    "sensors_status_imu"
]

# Extract data for explicit sensors
sensor_data = {}
for sensor in explicit_sensors:
    try:
        dataset = ulog.get_dataset(sensor)
        sensor_data[sensor] = pd.DataFrame(dataset.data)
    except KeyError:
        print(f"Dataset '{sensor}' not found in the ULog file.")

# Plot graphs for each explicit sensor
for sensor, data in sensor_data.items():
    plt.figure(figsize=(10, 6))
    
    if sensor == "sensor_accel" and all(col in data.columns for col in ['timestamp', 'x', 'y', 'z']):
        plt.plot(data['timestamp'].to_numpy(), data['x'].to_numpy(), label="Accel X")
        plt.plot(data['timestamp'].to_numpy(), data['y'].to_numpy(), label="Accel Y")
        plt.plot(data['timestamp'].to_numpy(), data['z'].to_numpy(), label="Accel Z")
        plt.xlabel("Timestamp")
        plt.ylabel("Acceleration (m/s²)")
        
    elif sensor == "sensor_baro" and 'pressure' in data.columns:
        plt.plot(data['timestamp'].to_numpy(), data['pressure'].to_numpy(), label="Barometric Pressure")
        plt.xlabel("Timestamp")
        plt.ylabel("Pressure (Pa)")
        

       
    elif sensor == "sensor_gps" and all(col in data.columns for col in ['lat', 'lon']):
        plt.plot(data['lon'].to_numpy(), data['lat'].to_numpy(), label="GPS Path")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        
    elif sensor == "sensor_gyro" and all(col in data.columns for col in ['timestamp', 'x', 'y', 'z']):
        plt.plot(data['timestamp'].to_numpy(), data['x'].to_numpy(), label="Gyro X")
        plt.plot(data['timestamp'].to_numpy(), data['y'].to_numpy(), label="Gyro Y")
        plt.plot(data['timestamp'].to_numpy(), data['z'].to_numpy(), label="Gyro Z")
        plt.xlabel("Timestamp")
        plt.ylabel("Angular Velocity (rad/s)")
        
    elif sensor == "sensor_mag" and all(col in data.columns for col in ['timestamp', 'x', 'y', 'z']):
        plt.plot(data['timestamp'].to_numpy(), data['x'].to_numpy(), label="Mag X")
        plt.plot(data['timestamp'].to_numpy(), data['y'].to_numpy(), label="Mag Y")
        plt.plot(data['timestamp'].to_numpy(), data['z'].to_numpy(), label="Mag Z")
        plt.xlabel("Timestamp")
        plt.ylabel("Magnetic Field Strength (µT)")
        
    elif sensor == "sensors_status_imu":
        for column in data.columns:
            if column != 'timestamp':
                plt.plot(data['timestamp'].to_numpy(), data[column].to_numpy(), label=column)
        plt.xlabel("Timestamp")
        plt.ylabel("IMU Status Indicators")
        
        #     elif sensor == "sensor_combined":
        # # Check if all relevant columns are present
        # if all(col in data.columns for col in ['timestamp', 'gyro_rad[0]', 'gyro_rad[1]', 'gyro_rad[2]', 
        #                                    'accelerometer_m_s2[0]', 'accelerometer_m_s2[1]', 'accelerometer_m_s2[2]', 
        #                                    'magnetometer_ga[0]', 'magnetometer_ga[1]', 'magnetometer_ga[2]']):
        
        #     # Plot gyroscope data
        #     plt.plot(data['timestamp'], data['gyro_rad[0]'], label="Gyro X (rad/s)")
        #     plt.plot(data['timestamp'], data['gyro_rad[1]'], label="Gyro Y (rad/s)")
        #     plt.plot(data['timestamp'], data['gyro_rad[2]'], label="Gyro Z (rad/s)")
            
        #     # Plot accelerometer data
        #     plt.plot(data['timestamp'], data['accelerometer_m_s2[0]'], label="Accel X (m/s²)", linestyle='dashed')
        #     plt.plot(data['timestamp'], data['accelerometer_m_s2[1]'], label="Accel Y (m/s²)", linestyle='dashed')
        #     plt.plot(data['timestamp'], data['accelerometer_m_s2[2]'], label="Accel Z (m/s²)", linestyle='dashed')
            
        #     # Plot magnetometer data
        #     plt.plot(data['timestamp'], data['magnetometer_ga[0]'], label="Mag X (Gauss)", linestyle='dotted')
        #     plt.plot(data['timestamp'], data['magnetometer_ga[1]'], label="Mag Y (Gauss)", linestyle='dotted')
        #     plt.plot(data['timestamp'], data['magnetometer_ga[2]'], label="Mag Z (Gauss)", linestyle='dotted')
            
        #     plt.xlabel("Timestamp")
        #     plt.ylabel("Sensor Data")
        #     plt.title("Combined Sensor Data (Accelerometer, Gyroscope, Magnetometer)")
        #     plt.legend()
        #     plt.grid(True)
        # else:
        #     print(f"Missing required columns in sensor_combined data: {list(data.columns)}")
    
    plt.title(f"{sensor.replace('_', ' ').capitalize()} Data")
    plt.legend()
    plt.grid(True)
    plt.show()
