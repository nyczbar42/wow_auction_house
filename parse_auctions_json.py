import requests
import json

item_ids = [
    210796, 210797, 210798, # Mycobloom
    210799, 210800, 210801, # Luredrop
    210802, 210803, 210804, # Orbinid
    210805, 210806, 210807, # Blessing Blossom
    210808, 210809, 210810, # Arathor's Spear
    210930, 210931, 210932, # Bismuth
    210933, 210934, 210935, # Aqirite
    210936, 210937, 210938, # Ironclaw Ore
    212667, 212668, 212669, # Gloom Chitin
    212670, 212672, 212673, # Thunderous Hide
    212674, 212675, 212676, # Sunless Carapace
]

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

def load_auctions_from_file(filename="eu_auctions.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error parsing file {filename}.")
        return None

def get_item_name(item_id, access_token, region="eu", namespace="static-eu"):
    url = f"https://{region}.api.blizzard.com/data/wow/item/{item_id}"
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
        item_data = response.json()
        return item_data.get("name", "Unknown Item")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving item name {item_id}: {e}.")
        return "Unknown Item"

def extract_lowest_item_prices(auctions_data, item_ids):
    lowest_prices = {item_id: float('inf') for item_id in item_ids}

    for auction in auctions_data.get("auctions", []):
        item_id = auction["item"]["id"]
        if item_id in item_ids:
            price = auction.get("unit_price") or auction.get("buyout", 0) // auction.get("quantity", 1)
            price_in_gold = price / 10000

            if price_in_gold < lowest_prices[item_id]:
                lowest_prices[item_id] = price_in_gold

    return {item_id: price for item_id, price in lowest_prices.items() if price < float('inf')}

def save_prices_to_file(item_prices, filename="item_prices.txt", access_token=None):
    try:
        with open(filename, "w") as file:
            for item_id, price in item_prices.items():
                item_name = get_item_name(item_id, access_token) if access_token else f"Item {item_id}"
                file.write(f"{item_name} - {price:.2f}\n")
        print(f"Prices have been saved to file {filename}.")
    except IOError as e:
        print(f"Error saving file: {e}.")

def main():
    token_file = "access_token.json"

    access_token = load_access_token_from_file(token_file)
    
    if not access_token:
        print("No token, terminating program")
        return

    auctions_data = load_auctions_from_file("eu_auctions.json")
    
    if not auctions_data:
        print("Failed to load auctions file.")
        return

    lowest_item_prices = extract_lowest_item_prices(auctions_data, item_ids)

    if lowest_item_prices:
        save_prices_to_file(lowest_item_prices, "item_prices.txt", access_token)
    else:
        print("Prices for the specified items not found.")

if __name__ == "__main__":
    main()
