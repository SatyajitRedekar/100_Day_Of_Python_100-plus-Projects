import os
import shutil

base_path = os.getcwd()

for folder in os.listdir(base_path):
    if os.path.isdir(folder) and folder.lower().startswith("day"):
        parts = folder.split()
        if len(parts) > 1 and parts[1].isdigit():
            day_num = int(parts[1])
            new_name = f"Day {day_num:02d}"   # Day 01, Day 02 ...
            if new_name != folder:
                shutil.move(folder, new_name)
                print(f"✅ Renamed {folder} → {new_name}")

print("\n🎯 All folders renamed with leading zeros.")
