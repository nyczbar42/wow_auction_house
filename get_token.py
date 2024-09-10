import requests
import json

def save_access_token_to_file(client_id, client_secret, filename="access_token.json"):
    url = "https://oauth.battle.net/token"
    auth = (client_id, client_secret)
    data = {"grant_type": "client_credentials"}
    
    try:
        response = requests.post(url, auth=auth, data=data)
        response.raise_for_status()
        token_data = response.json()

        with open(filename, "w") as file:
            json.dump(token_data, file)

        print(f"Token saved to file {filename}.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while obtaining the token: {e}")


client_id = "Client_ID"
client_secret = "Client_Secret"

save_access_token_to_file(client_id, client_secret)