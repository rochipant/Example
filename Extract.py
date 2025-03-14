import requests
import yaml

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def fetch_data():
    config = load_config()
    api_url = config['api']['url']
    api_key = config['api']['key']
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

if __name__ == "__main__":
    data = fetch_data()
    print(data)

