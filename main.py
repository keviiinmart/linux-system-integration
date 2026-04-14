import subprocess
import os

#Need psutil,time,datetime for System Monitor.py
import psutil
import time
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("---------- STARTING SYSTEM INTERGRATION ----------")

print("\n[1/3]\nRunning File Manager")
exec(open("scripts/file_manager.py").read())

print("\n[2/3]\nRunning System Monitor")
for i in range(3):
	cpu = psutil.cpu_percent()
	mem = psutil.virtual_memory().percent
	disk = psutil.disk_usage('/').percent
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	log_entry = f"{timestamp} | CPU: {cpu} | MEM: {mem}% | DISK: {disk}%\n"
	with open("logs/system.log", "a") as f:
		f.write(log_entry)
	print(log_entry.strip())
	time.sleep(5)

print("\n[3/3]\n Running Log Processor")
exec(open("scripts/log_processor.py").read())

print("---------- COMPLETE ----------")
