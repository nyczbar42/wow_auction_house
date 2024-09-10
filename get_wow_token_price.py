import requests
import json

def load_access_token_from_file(filename="access_token.json"):
    try:
        with open(filename, "r") as file:
            token_data = json.load(file)
            return token_data["access_token"]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except KeyError:
        print("Error reading token from file.")
        return None

def get_wow_token_price(access_token, region="eu", namespace="dynamic-eu"):
    url = f"https://{region}.api.blizzard.com/data/wow/token/index"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "namespace": namespace,
        "locale": "en_GB"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving WoW Token price: {e}")
        return None

def main():
    token_file = "access_token.json"
    
    access_token = load_access_token_from_file(token_file)
    
    if not access_token:
        print("No token found, terminating program.")
        return

    token_data = get_wow_token_price(access_token, region="eu", namespace="dynamic-eu")

    if token_data:
        token_price = token_data["price"] / 10000
        print(f"Current WoW Token price on EU server: {token_price:.2f} gold.")
    else:
        print("Failed to retrieve WoW Token price.")

if __name__ == "__main__":
    main()
