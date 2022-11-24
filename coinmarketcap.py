from requests import Request, Session
from requests import get
import credentials
import json

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
bitcoin_percent_24h = round(json.loads(response_bitcoin.text)["data"]["1"]["quote"]["EUR"]["percent_change_24h"], 2)
if bitcoin_percent_24h < -1:
    bitcoin_percent_24h_html = f"""
    <a style="color: red;">{bitcoin_percent_24h}</a>
    """    
elif bitcoin_percent_24h > 1:
    bitcoin_percent_24h_html = f"""
    <a style="color: green;">{bitcoin_percent_24h}</a>
    """    
else:
    bitcoin_percent_24h_html = f"""
    <a style="color: rgb(255, 179, 128);">{bitcoin_percent_24h}</a>
    """    
#Ethereum
response_ethereum = session.get(coins, params=ethereum)
ethereum_price = str(round(json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["price"], 2)) + " €"
ethereum_percent_24h = round(json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["percent_change_24h"], 2)
if ethereum_percent_24h < -1:
    ethereum_percent_24h_html = f"""
    <a style="color: red;">{ethereum_percent_24h}</a>
    """    
elif ethereum_percent_24h > 1:
    ethereum_percent_24h_html = f"""
    <a style="color: green;">{ethereum_percent_24h}</a>
    """    
else:
    ethereum_percent_24h_html = f"""
    <a style="color: rgb(255, 179, 128);">{ethereum_percent_24h}</a>
    """    

#ERGO
response_ergo = session.get(coins, params=ergo)
ergo_price = str(round(json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["price"], 2)) + " €"
ergo_price_number_only = json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["price"]
ergo_percent_24h = round(json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["percent_change_24h"], 2)
if ergo_percent_24h < -1:
    ergo_percent_24h_html = f"""
    <a style="color: red;">{ergo_percent_24h}</a>
    """    
elif ergo_percent_24h > 1:
    ergo_percent_24h_html = f"""
    <a style="color: green;">{ergo_percent_24h}</a>
    """    
else:
    ergo_percent_24h_html = f"""
    <a style="color: rgb(255, 179, 128);">{ergo_percent_24h}</a>
    """    

#Polkadot
response_polkadot = session.get(coins, params=polkadot)
polkadot_price = str(round(json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["price"], 2)) + " €"
polkadot_percent_24h = round(json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["percent_change_24h"], 2)
if polkadot_percent_24h < -1:
    polkadot_percent_24h_html = f"""
    <a style="color: red;">{polkadot_percent_24h}</a>
    """    
elif polkadot_percent_24h > 1:
    polkadot_percent_24h_html = f"""
    <a style="color: green;">{polkadot_percent_24h}</a>
    """    
else:
    polkadot_percent_24h_html = f"""
    <a style="color: rgb(255, 179, 128);">{polkadot_percent_24h}</a>
    """    

#Adding estimated rewards and profit
whattomine_api_keys = whattomine_api.json()
whattomine_api_keys.keys()
estimated_rewards_erg = whattomine_api_keys["coins"]["Ergo"]["estimated_rewards"]

#Electricity price example with 0.1€/kWh @ 26.4kWh/day
elec_price_kwh = 0.1
elec_consumption_24h = 26.4
elec_price_24h = elec_price_kwh * elec_consumption_24h
revenue_24h = float(estimated_rewards_erg) * ergo_price_number_only
profit_24h_eur = float(estimated_rewards_erg) * ergo_price_number_only - elec_price_24h


if profit_24h_eur >= 3:
    profit_24h_eur_html = f"""
    <a style="color: green;">{round(profit_24h_eur, 2)}</a>
    """    
elif profit_24h_eur <= -1.5:
    profit_24h_eur_html = f"""
    <a style="color: red;">{round(profit_24h_eur, 2)}</a>
    """    
else:
    profit_24h_eur_html = f"""
    <a style="color: rgb(255, 179, 128);">{round(profit_24h_eur, 2)}</a>
    """

#Print out a HTML file
estimated_profits_output = f"""
    <div style="font-size: 18px;">
        <a>Revenue 24h: {round(revenue_24h, 2)} €<br>
        Profit 24h: {profit_24h_eur_html} €<br>
        </a>
    <div>
    </html>
    """
#Print out a HTML file
coins_output = f"""
<table style="width: 96%; max-width: 400px; border: 2px solid rgb(255, 133, 51); background-color: black;">
    <tbody>
    <tr style="text-align: center; background-color: grey;">
    <td>Coin</td>
    <td>Price</td>
    <td>24H +/-</td>
    </tr>
    <tr style="text-align: center; background-color: rgb(216, 216, 216);">
    <td style="text-align: left;">BTC</td>
    <td style="text-align: left;">{bitcoin_price}</td>
    <td style="text-align: right;">{bitcoin_percent_24h_html} %</td>
    </tr>
    <tr style="text-align: center; background-color: #f1f1f1;">
    <td style="text-align: left;">ETH</td>
    <td style="text-align: left;">{ethereum_price}</td>
    <td style="text-align: right;">{ethereum_percent_24h_html} %</td>
    </tr>
    <tr style="text-align: center; background-color: rgb(216, 216, 216)";>
    <td style="text-align: left;">ERG</td>
    <td style="text-align: left;">{ergo_price}</td>
    <td style="text-align: right;">{ergo_percent_24h_html} %</td>
    </tr>
    <tr style="text-align: center; background-color: #f1f1f1;">
    <td style="text-align: left;">DOT</td>
    <td style="text-align: left;">{polkadot_price}</td>
    <td style="text-align: right;">{polkadot_percent_24h_html} %</td>
    </tr>
    </tbody>
</table>
"""

with open("/var/www/html/estimated_profits_output.html", "w", encoding="utf-8") as estimated_profits_file:
    estimated_profits_file.write(f"{estimated_profits_output}")

with open("/var/www/html/coins_output.html", "w", encoding="utf-8") as coinmarketcap_output_file:
    coinmarketcap_output_file.write(f"{coins_output}")
