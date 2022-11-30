from requests import get
from math import log, floor


#Function for changing large numbers to Kilos, Megas etc.
def hashrate_format(number):
    units = ['', ' KH', ' MH', ' GH', ' TH', ' PH']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f%s' % (number / k**magnitude, units[magnitude])


#The API for Herominers with my information
herominers_API = get("https://ergo.herominers.com/api/stats_address?address=9fbTRjsurmNp14mABUG3APak7TrxnbWnAuHv9NtW31oKPx2VgNV&recentBlocksAmount=20&longpoll=true")

#Extracting keys from the API
herominers_API_keys = herominers_API.json()
herominers_API_keys.keys()

#Hashrate data with fault tolerance in case of errors
try:
    current_hashrate = hashrate_format(herominers_API_keys["stats"]["hashrate"])
except Exception:
    current_hashrate = "No Hash"
    
try:
    avg_24h_hashrate = hashrate_format(herominers_API_keys["stats"]["hashrate_24h"])
except Exception:
    avg_24h_hashrate = "No Hash"
    
    
try:
    rig_1 = herominers_API_keys["workers"][1]["name"]
except Exception:
    rig_1 = "Cannot find Rig"
    
try:
    rig_2 = herominers_API_keys["workers"][0]["name"]
except Exception:
    rig_2 = "Cannot find Rig"
    
    
try:    
    rig_1_current_hashrate = hashrate_format(herominers_API_keys["workers"][1]["hashrate"])
except Exception:
    rig_1_current_hashrate = "Offline"
    
try:
    rig_2_current_hashrate = hashrate_format(herominers_API_keys["workers"][0]["hashrate"])
except Exception:
    rig_2_current_hashrate = "Offline"
    
#ERGO Payment data, rounded to 2 decimals
try:
    total_paid_ergo = int(herominers_API_keys["stats"]["paid"]) / 1000000000
    total_paid_ergo = round(total_paid_ergo, 2)
except Exception:
    total_paid_ergo = "Cannot fetch balance"
    
try:
    pending_balance_ergo = int(herominers_API_keys["stats"]["balance"]) / 1000000000
    pending_balance_ergo = round(pending_balance_ergo, 2)
except Exception:
    pending_balance_ergo = "Cannot fetch balance"
    


herominers_output = f"""
<a>{rig_1}: {rig_1_current_hashrate}<br>
{rig_2}: {rig_2_current_hashrate}<br>
Total: {current_hashrate}<br>
Total 24H: {avg_24h_hashrate}
"""
ergo_output = f"""
<a>Ergo<br>
Total paid: {total_paid_ergo}<br>
Pending: {pending_balance_ergo}</a>
"""