from requests import Request, Session
from requests import get
import credentials
import json



try:
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
    bitcoin_price = json.loads(response_bitcoin.text)["data"]["1"]["quote"]["EUR"]["price"]
    bitcoin_percent_24h = json.loads(response_bitcoin.text)["data"]["1"]["quote"]["EUR"]["percent_change_24h"]

    #Ethereum
    response_ethereum = session.get(coins, params=ethereum)
    ethereum_price = json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["price"]
    ethereum_percent_24h = json.loads(response_ethereum.text)["data"]["1027"]["quote"]["EUR"]["percent_change_24h"]

    #ERGO
    response_ergo = session.get(coins, params=ergo)
    ergo_price = json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["price"]
    ergo_percent_24h = json.loads(response_ergo.text)["data"]["1762"]["quote"]["EUR"]["percent_change_24h"]

    #Polkadot
    response_polkadot = session.get(coins, params=polkadot)
    polkadot_price = json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["price"]
    polkadot_percent_24h = json.loads(response_polkadot.text)["data"]["6636"]["quote"]["EUR"]["percent_change_24h"]

    #Adding estimated rewards and profit
    whattomine_api_keys = whattomine_api.json()
    whattomine_api_keys.keys()
    estimated_rewards_erg = whattomine_api_keys["coins"]["Ergo"]["estimated_rewards"]

    #Electricity price example with 0.1€/kWh @ 26.4kWh/day
    elec_price_kwh = 0.1
    elec_consumption_24h = 26.4
    elec_price_24h = elec_price_kwh * elec_consumption_24h
    revenue_24h = float(estimated_rewards_erg) * ergo_price
    profit_24h_eur = float(estimated_rewards_erg) * ergo_price - elec_price_24h


    #Functions to determine output colors based on given values

    def coin_color(x):
        red = f"""
        "<span style="color: red"{x}</span>
        """
        orange = f"""
        <span style="color: rgba(255, 145, 1);">{x}</span>
        """
        green = f"""
        <span style="color: green;">{x}</span>
        """
        
        if x < -1:
            output = red
        elif x > 1:
            output = green
        else:
            output = orange

        return output


    def profit_color(x):
        red = f"""
        <span style="color: red">{x}</span>
        """
        orange = f"""
        <span style="color: yellow;">{x}</span>
        """
        green = f"""
        <span style="color: green;">{x}</span>
        """
        
        if x >= 3:
            x = red
        elif x <= -1.5:
            x = green
        else:
            x = orange
            
        return x


    #Output as HTML
    coins_output = f"""
	<table class="demTable">
		<thead>
			<tr>
				<th>Coin</th>
				<th>Price</th>
				<th>24H +/-</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>BTC</td>
				<td>{round(bitcoin_price, 2)} €</td>
				<td>{coin_color(round(bitcoin_percent_24h, 2))} %</td>
			</tr>
			<tr>
				<td>ETH</td>
				<td>{round(ethereum_price, 2)} €</td>
				<td>{coin_color(round(ethereum_percent_24h, 2))} %</td>
			</tr>
			<tr>
				<td>ERG</td>
				<td>{round(ergo_price, 2)} €</td>
				<td>{coin_color(round(ergo_percent_24h, 2))} %</td>
			</tr>
			<tr>
				<td>DOT</td>
				<td>{round(polkadot_price, 2)} €</td>
				<td>{coin_color(round(polkadot_percent_24h, 2))} %</td>
			</tr>
		</tbody>
	</table>
    """
    

    profit_24h_eur = f"""
    <a style="font-size: 3.5vw;">{profit_color(round(profit_24h_eur, 2))} €</a>
    """
    revenue_24h = f"""
    <a style="font-size: 2.5vw;">{round(revenue_24h, 2)} €</a>
    """

except Exception:
        coins_output = f"""
        <a>Data load error.</a>
        """
        