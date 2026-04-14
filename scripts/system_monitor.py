import psutil
import time
from datetime import datetime

while True:
	cpu = psutil.cpu_percent()
	mem = psutil.virtual_memory().percent
	disk = psutil.disk_usage('/').percent
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	log_entry = f"{timestamp} | CPU : {cpu}% | MEM : {mem}% | Disk : {disk}%\n"

	with open("logs/system.log", "a") as f:
		f.write(log_entry)

	print(log_entry.strip())
	time.sleep(30)
