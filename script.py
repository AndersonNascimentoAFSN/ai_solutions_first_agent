import glob
import os
from pathlib import Path

# from pathlib import Path
# data_folder = Path(__file__).parent / "data"
# print(f"Data folder path: {data_folder}")

# project_root = os.getcwd()
# data_dir = os.path.join(project_root, "data")
# os.makedirs(data_dir, exist_ok=True)
# print(f"Data folder path: {data_dir}")

# pattern = os.path.join(data_dir, "**", "*.csv")
# csv_paths = glob.glob(pattern, recursive=True)

# print(f"CSV files in the root data directory: {csv_paths}")

project_root = Path(__file__).parent.parent.parent  # se o script estiver em app.py no root do projeto
data_dir = project_root / "data"
print(f"Project root path: {data_dir}")
data_dir.mkdir(parents=True, exist_ok=True)