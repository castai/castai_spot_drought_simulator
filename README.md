# CAST.AI Spot Drought Tool

This script provides a simple utility to manage the spot instance type blacklist for your CAST.AI cluster. It offers functionalities such as adding instance families to the blacklist, viewing the current blacklist, and removing instance families from the blacklist.

## Features

- Automatically extract instance families from the CAST.AI filter instance types API.
- Interactively add or remove instance families from the CAST.AI inventory blacklist.
- Display the current list of blacklisted instance families.

## Prerequisites

- Python 3.x
- The `requests` module (can be installed via pip: `pip install requests`)

## Configuration

You need to set the following environment variable:

- **CASTAI_API_KEY**: This should contain your CAST.AI API key.

The script also contains placeholders for `CASTAI_ORGANIZATION_ID` and `CASTAI_CLUSTER_ID`, which you should update with appropriate values before executing the script.

## Usage

1. Make sure you have set the necessary environment variable and updated the organization and cluster IDs in the script.
2. Run the script:
   `python castai_spot_drought.py`
3. The script will launch in interactive mode. Follow the on-screen instructions to manage the blacklist.

## Interactive Mode

Upon launching the script, you will be presented with the following options:

1. Add to blacklist
2. Get blacklist
3. Remove from blacklist
4. Exit

Select the appropriate option by entering the corresponding number.

## Important Notes

- Ensure that you have the necessary permissions in your CAST.AI account to interact with the API endpoints utilized by this script.
- Always double-check the blacklist before and after making modifications to ensure accuracy and avoid unintended disruptions.

## Contributing

If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

