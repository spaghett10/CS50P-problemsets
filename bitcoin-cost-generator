"""
Implement a program that:
Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. 
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. 
You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
"""


import requests
import sys

def main():
    #Verify request success
    try:
        bit_api = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2de4ba5530d6dc1629076bb996eabbb720947ebb77d9386132a17ed3a1ccf38e")
    except requests.RequestException:
        sys.exit()

    bit_json = bit_api.json()
    unit_price = float(bit_json["data"]["priceUsd"]) #After validation of request, store bitcoin price in unit_price variable

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument") #Exit program if user has not put in quantity command-line argument

    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number") #Exit program if non-numeric value entered

    total_price = unit_price * float(sys.argv[1]) #Calculate output price

    print(f"${total_price:,.4f}") #Print price to four decimal places with comma separator

main()
