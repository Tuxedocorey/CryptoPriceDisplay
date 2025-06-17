# CryptoPriceDisplay
# This program should find the price and % 24 hr change of Bitcoin, Ethereum, Solana, and XRP and display it on LCD.
# Corey R
# API KEY: ####

import serial
import os

os.system("cls")
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# initialize arduino
arduino = serial.Serial(port="COM3", baudrate=115200, timeout=0.1)
time.sleep(2)


def coinPrice(unrounded, name):  # Function prints rounded price of chosen crypto
    price = round(unrounded, 2)
    return price


def priceChange(change):
    return round(change, 2)


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"  # Endpoint
parameters = {
    "start": "1",
    "limit": "5000",
    "convert": "USD",  # Chosen currency to convert to
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "XXXXX",  # INSERT API KEY HERE
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print("Success!")  # Outputs if everything works.

    # fetches prices
    btcPrice = data["data"][0]["quote"]["USD"]["price"]
    ethPrice = data["data"][1]["quote"]["USD"]["price"]
    # parses JSON data and grabs price from API
    xrpPrice = data["data"][3]["quote"]["USD"]["price"]
    solPrice = data["data"][5]["quote"]["USD"]["price"]

    # fethes percent change
    btcChange = data["data"][0]["quote"]["USD"]["percent_change_24h"]
    ethChange = data["data"][1]["quote"]["USD"]["percent_change_24h"]
    xrpChange = data["data"][3]["quote"]["USD"]["percent_change_24h"]
    solChange = data["data"][5]["quote"]["USD"]["percent_change_24h"]

    # loop that will prompt users to choose a crpyto
    while True:
        choice = int(
            input(
                "Pick a crypto to see day change\n1. BTC\n2. ETH\n3. XRP\n4. SOL\nChoice: "
            )
        )
        if choice < 0 or choice > 4:
            print("Error! Please select a number 1-4")
            time.sleep(2)
        else:
            break

    ###TEST THIS BLOCK###
    # match statement that sends price change to ardunio
    match choice:
        case 1:
            print(f"Price change is: %{priceChange(btcChange)}")

            arduino.write(
                bytes(
                    f"Price: {coinPrice(btcPrice,2)}, Change: {priceChange(btcChange)}",
                    "utf-8",
                )
            )

        case 2:
            print(f"Price change is: %{priceChange(ethChange)}")
            arduino.write(
                bytes(
                    f"Price: {coinPrice(ethPrice,2)}, Change: {priceChange(ethChange)}",
                    "utf-8",
                )
            )

        case 3:
            print(f"Price change is: %{priceChange(xrpChange)}")
            arduino.write(
                bytes(
                    f"Price: {coinPrice(xrpPrice,2)}, Change: {priceChange(xrpChange)}",
                    "utf-8",
                )
            )

        case 4:
            print(f"Price change is: %{priceChange(solChange)}")
            arduino.write(
                bytes(
                    f"Price: {coinPrice(solPrice,2)}, Change: {priceChange(solChange)}",
                    "utf-8",
                )
            )

        case _:
            print("An error occurred")
    ###


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print("Error, connection failed")
    print(e)
