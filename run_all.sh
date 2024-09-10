#!/bin/sh

run_python_script() {
    script_name=$1
    echo "Running script: $script_name"
    python3 "$script_name"
    if [ $? -ne 0 ]; then
        echo "An error occurred while running $script_name"
        exit 1
    fi
}

if [ ! -f "access_token.json" ]; then
    echo "Missing access_token.json file. Fetching a new token..."
    run_python_script "get_token.py"
fi

echo "Fetching auction data..."
run_python_script "get_auctions.py"

echo "Processing auction data..."
run_python_script "parse_auctions_json.py"

echo "All scripts have been successfully run."
