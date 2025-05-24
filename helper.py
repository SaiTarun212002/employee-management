import json
import os
DATA_FILE="D:\\fastapi\\database\\employedata.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)