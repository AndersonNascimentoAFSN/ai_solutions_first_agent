# from pathlib import Path
# data_folder = Path(__file__).parent / "data"
# print(f"Data folder path: {data_folder}")

import glob
import os
project_root = os.getcwd()
data_dir = os.path.join(project_root, "data")
os.makedirs(data_dir, exist_ok=True)
print(f"Data folder path: {data_dir}")

pattern = os.path.join(data_dir, "**", "*.csv")
csv_paths = glob.glob(pattern, recursive=True)

print(f"CSV files in the root data directory: {csv_paths}")