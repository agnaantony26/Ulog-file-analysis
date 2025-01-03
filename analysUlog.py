import pyulog
import os
import json
# Path to the uploaded ULog file
ulog_file_path = '/Users/agna/Downloads/log_0_2024-11-8-14-14-58.ulg'

# Attempt to load the ULog file and inspect its metadata and available data
try:
    if not os.path.exists(ulog_file_path):
        raise FileNotFoundError(f"File not found: {ulog_file_path}")
    ulog = pyulog.ULog(ulog_file_path)
    #print(dir(ulog))

    # Extract metadata and available data fields for initial analysis
    
    initial_metadata = {
        #"version": version_info,
        "log_start_timestamp": ulog.start_timestamp,
        "log_end_timestamp": ulog.last_timestamp,
        "message_names": [elem.name for elem in ulog.data_list],
    }
    #print(initial_metadata)
    with open('initial_metadata.json', 'w') as f:
        json.dump(initial_metadata, f, indent=4)
except Exception as e:
    print(f"Error loading ULog file: {e}")




