with open("logs/system.log", "r") as f:
	lines = f.readlines()

print("---------- SYSTEM LOG ANALYSIS ----------")
for line in lines:
	if "CPU" in line:
		raw = line.split("CPU:")[1].split("|")[0].strip()
		print(f"DEBUG raw value: '{raw}'")
		cpu_val = float(raw)
		if cpu_val > 80:
			print(f" !!!!!! HIGH CPU ALERT: {line.strip()} !!!!!!")
		else:
			print(f"Normol: {line.strip()}")
