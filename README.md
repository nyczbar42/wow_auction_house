# Scripts for Fetching and Processing World of Warcraft Auction Data

This project contains scripts for fetching auction data from the World of Warcraft game, processing it, and saving the results to a file. The scripts use the Battle.net API to retrieve auction and item price information on EU servers.

## Scripts

### `run_all.sh`

This bash script runs all the following scripts in the correct order:

1. Checks if the `access_token.json` file exists, and if not, runs `get_token.py` to fetch a token.
2. Runs `get_auctions.py` to fetch auction data.
3. Runs `parse_auctions_json.py` to process the data and save the results to `item_prices.txt`.

#### How to Run:
1. Register an application on the Blizzard Developer Portal and obtain an API key (Client ID and Client Secret).
2. Enter your Client ID and Client Secret into the `get_token.py` file's `client_id` and `client_secret` variables.
3. Specify the items whose prices you want to check in the `parse_auctions_json.py` file.
4. Ensure that you have Python and the `requests` library installed and that you have made the `run_all.sh` script executable:
   ```sh
   chmod +x run_all.sh
5. Run the script:
   ```sh
   ./run_all.sh

The scripts will create the ```item_prices.txt``` file and save the item prices in it. 
Below are the descriptions of the individual scripts and instructions for running them without using ```run_all.sh```.

### `get_token.py`

This script fetches an access token for the Battle.net API and saves it to the ```access_token.json``` file. The token is required for API request authorization.

#### How to Run:
1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python3 get_token.py


### `get_auctions.py`

This script fetches auction data from the Battle.net API and saves it to the ```eu_auctions.json``` file. The script uses the access token from the ```access_token.json``` file.

#### How to Run:
1. Ensure you have Python installed and the ```access_token.json``` file with a valid token.
2. Run the script:
   ```sh
   python3 get_auctions.py

### `parse_auctions_json.py`

This script processes data from the ```eu_auctions.json``` file and saves the lowest item prices to the ```item_prices.txt``` file. The script extracts item prices and names in a user-friendly format.

#### How to Run:
1. Ensure you have Python installed and the ```eu_auctions.json``` file with current auction data.
2. Run the script:
   ```sh
   python3 parse_auctions_json.py

## Requirements:

- Python 3.x
- Python Libraries: requests (install via pip install requests)
- Internet access (to fetch data from the Battle.net API)

## Notes
- The scripts assume you have an active Battle.net account and appropriate permissions to use the API.
- The access token is valid for a specific period, so it may need to be refreshed if necessary.