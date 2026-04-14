import os
import shutil

watch_folder = "data"
destinations = {
	".log": "logs",
	".csv": "data",
	".txt": "reports"
}

files = os.listdir(watch_folder)
for file in files:
	ext = os.path.splitext(file)[1]
	if ext in destinations:
		src = os.path.join(watch-folder, file)
		dst = os.path.koin(destinations[ext], file)
		shutil.move(src,dst)
		print(f"Moved {file} -> {destinations[ext]}/")
