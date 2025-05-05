from pathlib import Path
import sys

PARENT_PATH = Path(__file__).resolve().parent.parent

sys.path.append(f"{PARENT_PATH}")
sys.path.append(f"{PARENT_PATH}/src")
