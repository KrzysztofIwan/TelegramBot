import json

def load_token(file_path='data/setup_api.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['token']