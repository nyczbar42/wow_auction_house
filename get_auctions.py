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

def get_auctions(access_token, region="eu", namespace="dynamic-eu"):
    url = f"https://{region}.api.blizzard.com/data/wow/auctions/commodities"
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
        print(f"Error retrieving auction: {e}")
        return None

def save_auctions_to_file(auctions_data, filename="eu_auctions.json"):
    try:
        with open(filename, "w") as file:
            json.dump(auctions_data, file, indent=4)
        print(f"Auctions have been saved to file {filename}.")
    except IOError as e:
        print(f"Error saving file: {e}.")

def main():
    token_file = "access_token.json"
    
    access_token = load_access_token_from_file(token_file)
    
    if not access_token:
        print("Missing token, terminating program.")
        return

    auctions_data = get_auctions(access_token, region="eu", namespace="dynamic-eu")

    if auctions_data:
        save_auctions_to_file(auctions_data, "eu_auctions.json")
    else:
        print("Failed to retrieve auctions.")

if __name__ == "__main__":
    main()
