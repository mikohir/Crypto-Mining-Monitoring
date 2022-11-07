from requests import Request, Session
from requests import get
import credentials
import json
from tabulate import tabulate

#URLs
whattomine_api = get("https://whattomine.com/coins.json?factor%5Beth_hr%5D=174.0&factor%5Beth_p%5D=540.0&factor%5Be4g_hr%5D=175.8&factor%5Be4g_p%5D=540.0&factor%5Bzh_hr%5D=198.0&factor%5Bzh_p%5D=540.0&factor%5Bcnh_hr%5D=3900.0&factor%5Bcnh_p%5D=540.0&factor%5Bcng_hr%5D=6900.0&factor%5Bcng_p%5D=540.0&factor%5Bcnf_hr%5D=6600.0&factor%5Bcnf_p%5D=540.0&factor%5Bcx_hr%5D=0.0&factor%5Bcx_p%5D=0.0&factor%5Beqa_hr%5D=900.0&factor%5Beqa_p%5D=540.0&factor%5Bcc_hr%5D=25.8&factor%5Bcc_p%5D=540.0&factor%5Bcr29_hr%5D=25.8&factor%5Bcr29_p%5D=540.0&factor%5Bhh_hr%5D=1500.0&factor%5Bhh_p%5D=540.0&factor%5Bct32_hr%5D=1.32&factor%5Bct32_p%5D=540.0&factor%5Beqb_hr%5D=84.6&factor%5Beqb_p%5D=540.0&factor%5Brmx_hr%5D=3180.0&factor%5Brmx_p%5D=540.0&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=1140.0&factor%5Bal_p%5D=1100.0&factor%5Bops_hr%5D=134.4&factor%5Bops_p%5D=600.0&factor%5Beqz_hr%5D=117.0&factor%5Beqz_p%5D=540.0&factor%5Bzlh_hr%5D=144.0&factor%5Bzlh_p%5D=540.0&factor%5Bkpw_hr%5D=64.2&factor%5Bkpw_p%5D=540.0&factor%5Bppw_hr%5D=67.8&factor%5Bppw_p%5D=600.0&factor%5Bx25x_hr%5D=17.4&factor%5Bx25x_p%5D=540.0&factor%5Bfpw_hr%5D=60.0&factor%5Bfpw_p%5D=540.0&factor%5Bvh_hr%5D=2.76&factor%5Bvh_p%5D=540.0&factor%5Bcost%5D=0.1&factor%5Bcost_currency%5D=USD&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main")
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
ergo_price_number_only = json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["price"]
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


#Adding estimated rewards and profit
whattomine_api_keys = whattomine_api.json()
whattomine_api_keys.keys()
estimated_rewards_erg = whattomine_api_keys["coins"]["Ergo"]["estimated_rewards"]

#Electricity price example with 0.1€/kWh @ 26.4kWh/day
elec_price_kwh = 0.1
elec_consumption_24h = 26.4
elec_price_24h = elec_price_kwh * elec_consumption_24h
estimated_profit_24h = float(estimated_rewards_erg) * ergo_price_number_only
estimated_profit_24h_eur_after_elec = float(estimated_rewards_erg) * ergo_price_number_only - elec_price_24h



#Output
with open("/var/www/html/estimated_profits_output.txt", "w", encoding="utf-8") as estimated_profits_file:
    estimated_profits_file.write(f"Estimated 24h profit: {round(estimated_profit_24h, 2)} €\n")
    estimated_profits_file.write(f"After electricity: {round(estimated_profit_24h_eur_after_elec, 2)} €")

with open("/var/www/html/coinmarketcap_output.txt", "w", encoding="utf-8") as coinmarketcap_output_file:
    coinmarketcap_output_file.write(tabulate(combined_list, headers=["Coin", "Price", "24H +/-"], tablefmt="fancy_grid"))
