# Windows System Performance Monitor

This Python project monitors Windows system performance (CPU, RAM, Disk, and Network usage), logs the data to a CSV file, and generates a textual summary report of the collected data. The project also triggers alert messages (via console output) if any resource usage exceeds predefined thresholds.

## Features

- **Real-time Monitoring:** Uses the `psutil` library to measure:
  - **CPU Usage:** Sampled every 1 second.
  - **RAM Usage:** Percentage of virtual memory used.
  - **Disk Usage:** Percentage used on a specified drive (e.g., `C:\`).
  - **Network I/O:** Bytes sent and received.
  
- **CSV Logging:** Writes all performance metrics with a timestamp into a CSV file (`system_performance.csv`) at a configurable interval.

- **Threshold Alerts:** Prints alert messages if:
  - CPU usage exceeds 90%
  - RAM usage exceeds 90%
  - Disk usage exceeds 95%

- **Summary Report:** After logging data for a specified duration, the script reads the CSV file using Python’s built-in `csv` module and prints a summary report. The report includes:
  - Average and maximum CPU, RAM, and Disk usage.
  - The total number of data points and the time range of data collection.

## Requirements

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)
  
  ```bash
  pip install psutil
Configuration
You can modify the following configuration variables in the script to suit your needs:

LOG_CSV: Name or path of the CSV file for logging data.
LOG_INTERVAL: Interval (in seconds) between data logging.
DURATION: Total duration (in seconds) for logging (for demonstration purposes).
For continuous monitoring, you can change the logging loop to run indefinitely.
CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD: Resource usage thresholds for triggering alerts.
For disk usage, ensure the drive path (e.g., 'C:\\') matches your Windows system setup.
How It Works
Logging Performance Data:

The script initializes a CSV file with headers for timestamp, CPU, RAM, disk, and network metrics.
It collects performance data every LOG_INTERVAL seconds and writes each record to the CSV file.
Alerts are printed to the console if any resource usage exceeds its threshold.
Generating a Report:

After the logging period (or when you stop the script), the CSV file is read.
The script computes the average and maximum values for CPU, RAM, and disk usage.
A summary report is printed to the console, showing the data statistics and the time range of data collection.
