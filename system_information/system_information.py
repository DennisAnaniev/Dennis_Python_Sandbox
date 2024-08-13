import psutil
import datetime

print("========General Information=========")
boot_time = psutil.boot_time()
boot_datetime = datetime.datetime.fromtimestamp(boot_time)
formatted_boot_time = boot_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Boot Time: {formatted_boot_time}")

print("========CPU Information=========")
print(psutil.cpu_count(logical=False))
print(psutil.cpu_percent(percpu=True))
print(psutil.getloadavg())

print("========RAM Information=========")
virtual_memory = psutil.virtual_memory()
print(f"Total memory in GB:  {virtual_memory.total/1024/1024/1024:.2f} GB")
swap_memory = psutil.swap_memory()
print(f"Total swap memory in GB:  {swap_memory.total/1024/1024/1024:.2f} GB")
usage_percent = virtual_memory.percent
print(f"Used Memory: {usage_percent}%")

print("========Disk Information=========")
print(psutil.disk_partitions())
disk = psutil.disk_usage('/')
total_gb = disk.total / (1024 * 1024 * 1024)
used_gb = disk.used / (1024 * 1024 * 1024)
free_gb = disk.free / (1024 * 1024 * 1024)

print(f"Total Disk Space: {total_gb:.2f} GB") # Format to 2 decimal places
print(f"Used Disk Space: {used_gb:.2f} GB")
print(f"Free Disk Space: {free_gb:.2f} GB")

percent_used = (disk.used / disk.total) * 100
print(f"Disk Usage: {percent_used:.2f}%")

print("========Network=========")
print(psutil.net_connections())
print(psutil.net_if_stats())