
import psutil
import time
from logger import save_log



print("server Health monitor")
print("Program started successfully!")
def get_cpu_usage():
   return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent


def get_network_usage():
    network = psutil.net_io_counters()

    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv

    return bytes_sent, bytes_received


def convert_bytes(bytes_value):
    return bytes_value / (1024 * 1024)

def get_status(usage):
    
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 70:
        return "WARNING"
    else:
        return "NORMAL"

def get_health_status(cpu, memory, disk):
    cpu_status = get_status(cpu)
    memory_status = get_status(memory)
    disk_status = get_status(disk)

    if "CRITICAL" in [cpu_status, memory_status, disk_status]:
        overall_status = "CRITICAL"
    elif "WARNING" in [cpu_status, memory_status, disk_status]:
        overall_status = "WARNING"
    else:
        overall_status = "NORMAL"

    return cpu_status, memory_status, disk_status, overall_status

def display_health_report(cpu, memory, disk, sent_mb, received_mb):
    print("===============================")
    print("         SERVER HEALTH")
    print("===============================")

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Data Sent: {sent_mb:.2f} MB")
    print(f"Data Received: {received_mb:.2f} MB")

    print("===============================")


def main():
    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()
        bytes_sent, bytes_received = get_network_usage()


        sent_mb = convert_bytes(bytes_sent)
        received_mb = convert_bytes(bytes_received)

        cpu_status, memory_status, disk_status, status = get_health_status(
            cpu, memory, disk
        )

        display_health_report(cpu, memory, disk, sent_mb, received_mb)

        print(f"CPU Status: {cpu_status}")
        print(f"Memory Status: {memory_status}")
        print(f"Disk Status: {disk_status}")
        print(f"Server Status: {status}")

        save_log(
            f"CPU: {cpu}% ({cpu_status}) | "
            f"Memory: {memory}% ({memory_status}) | "
            f"Disk: {disk}% ({disk_status}) | "
            f"Status: {status}"
        )


        time.sleep(10)
if __name__ == "__main__":
    main()

