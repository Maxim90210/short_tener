import json
import os

FILE_PATH = 'url_data.json'

def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

def get_url(short_id):
    data = load_data()
    return data.get(short_id)

def save_url(short_id, original_url):
    data = load_data()
    data[short_id] = original_url
    save_data(data)
