import psutil
import csv
import time
import datetime

# -------------------- CONFIGURATION --------------------
LOG_CSV = "system_performance.csv"  # CSV file to store performance data
LOG_INTERVAL = 5  # Interval (in seconds) between logs
DURATION = 60  # Total duration (in seconds) for logging (for demo; adjust as needed)

# Thresholds for alerts (in percentage)
CPU_THRESHOLD = 90.0  # CPU usage alert if > 90%
RAM_THRESHOLD = 90.0  # RAM usage alert if > 90%
DISK_THRESHOLD = 95.0  # Disk usage alert if > 95%


# --------------------------------------------------------

def log_performance_data():
    """Logs system performance data to a CSV file and triggers alerts if thresholds are exceeded."""
    with open(LOG_CSV, mode='w', newline='') as csvfile:
        fieldnames = ['timestamp', 'cpu_percent', 'ram_percent', 'disk_percent', 'net_sent', 'net_recv']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        start_time = time.time()
        while time.time() - start_time < DURATION:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Capture performance metrics
            cpu = psutil.cpu_percent(interval=1)  # 1-second sampling for CPU
            ram = psutil.virtual_memory().percent
            # For Windows, use the appropriate drive letter (e.g., 'C:\\')
            disk = psutil.disk_usage('C:\\').percent
            net = psutil.net_io_counters()
            net_sent = net.bytes_sent
            net_recv = net.bytes_recv

            # Log data to CSV
            writer.writerow({
                'timestamp': timestamp,
                'cpu_percent': cpu,
                'ram_percent': ram,
                'disk_percent': disk,
                'net_sent': net_sent,
                'net_recv': net_recv
            })
            print(f"{timestamp} | CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

            # Check thresholds and trigger alerts if exceeded
            if cpu > CPU_THRESHOLD:
                print(f"ALERT: CPU usage high at {cpu}%")
            if ram > RAM_THRESHOLD:
                print(f"ALERT: RAM usage high at {ram}%")
            if disk > DISK_THRESHOLD:
                print(f"ALERT: Disk usage high at {disk}%")
            # Wait for the remainder of the LOG_INTERVAL (subtracting the 1 sec used for CPU sampling)
            time.sleep(max(0, LOG_INTERVAL - 1))
    print("Logging complete.")


def generate_csv_report():
    """Reads the CSV log file and generates a summary report using the csv module."""
    cpu_values = []
    ram_values = []
    disk_values = []
    timestamps = []

    with open(LOG_CSV, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                timestamps.append(datetime.datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'))
                cpu_values.append(float(row['cpu_percent']))
                ram_values.append(float(row['ram_percent']))
                disk_values.append(float(row['disk_percent']))
            except Exception as e:
                print("Error processing row:", e)

    if not cpu_values:
        print("No data found in CSV log file.")
        return

    avg_cpu = sum(cpu_values) / len(cpu_values)
    avg_ram = sum(ram_values) / len(ram_values)
    avg_disk = sum(disk_values) / len(disk_values)

    max_cpu = max(cpu_values)
    max_ram = max(ram_values)
    max_disk = max(disk_values)

    print("\nSummary Report:")
    print("----------------------------")
    print(f"Data points: {len(cpu_values)}")
    print(f"Average CPU Usage: {avg_cpu:.2f}% (Max: {max_cpu:.2f}%)")
    print(f"Average RAM Usage: {avg_ram:.2f}% (Max: {max_ram:.2f}%)")
    print(f"Average Disk Usage: {avg_disk:.2f}% (Max: {max_disk:.2f}%)")

    start_time = min(timestamps)
    end_time = max(timestamps)
    print(f"Data collected from {start_time} to {end_time}")


if __name__ == "__main__":
    # Log system performance data for the specified duration
    log_performance_data()
    # Generate and print a summary report using the csv module
    generate_csv_report()
