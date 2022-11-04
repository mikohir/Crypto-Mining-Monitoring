from requests import Request, Session
from requests import get
import credentials
import json
from tabulate import tabulate

#URLs
coins = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

#Parameters
bitcoin = {
    "slug": "bitcoin",
    "convert": "EUR",
    }

ethereum = {
    "slug": "ethereum",
    "convert": "EUR",
    }

ergo = {
    "slug": "ergo",
    "convert": "EUR",
    }

polkadot = {
    "slug": "polkadot",
    "convert": "EUR",
    }

#Headers
headers = { 
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": credentials.coinmarketcap_key,
    }

#Session
session = Session()
session.headers.update(headers)

#Responses
#Bitcoin
response_bitcoin = session.get(coins, params=bitcoin)
bitcoin_price = str(round(json.loads(response_bitcoin.text)["data"]["1"]["quote"]["EUR"]["price"], 2)) + " €"
bitcoin_percent_24h = str(round(json.loads(response_bitcoin.text)["data"]["1"]["quote"]["EUR"]["percent_change_24h"], 2)) + " %"

#Ethereum
response_ethereum = session.get(coins, params=ethereum)
ethereum_price = str(round(json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["price"], 2)) + " €"
ethereum_percent_24h = str(round(json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["percent_change_24h"], 2)) + " %"

#ERGO
response_ergo = session.get(coins, params=ergo)
ergo_price = str(round(json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["price"], 2)) + " €"
ergo_percent_24h = str(round(json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["percent_change_24h"], 2)) + " %"

#Polkadot
response_polkadot = session.get(coins, params=polkadot)
polkadot_price = str(round(json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["price"], 2)) + " €"
polkadot_percent_24h = str(round(json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["percent_change_24h"], 2)) + " %"

#Create a lists
btc_list = ["BTC", bitcoin_price, bitcoin_percent_24h]
eth_list = ["ETH", ethereum_price, ethereum_percent_24h]
erg_list = ["ERG", ergo_price, ergo_percent_24h]
dot_list = ["DOT", polkadot_price, polkadot_percent_24h]
combined_list = [btc_list, eth_list, erg_list, dot_list]

#Output with tabulate
with open("/var/www/html/coinmarketcap_output.txt", "w", encoding="utf-8") as coinmarketcap_output_file:
    coinmarketcap_output_file.write(tabulate(combined_list, headers=["Coin", "Price", "24H +/-"], tablefmt="fancy_grid"))
