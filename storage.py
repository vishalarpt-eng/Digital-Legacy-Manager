import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "assets.json"


def load_assets():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_assets(assets):
    DATA_DIR.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(assets, file, indent=4)