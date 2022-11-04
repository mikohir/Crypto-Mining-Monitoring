from requests import get
from math import log, floor

def herominers_requests():

    #The API for Herominers with my information
    herominers_API = get("https://ergo.herominers.com/api/stats_address?address=9fbTRjsurmNp14mABUG3APak7TrxnbWnAuHv9NtW31oKPx2VgNV&recentBlocksAmount=20&longpoll=true")

    #Extracting keys from the API
    herominers_API_keys = herominers_API.json()
    herominers_API_keys.keys()

    #Hashrate data
    current_hashrate = herominers_API_keys["stats"]["hashrate"]
    avg_24h_hashrate = herominers_API_keys["stats"]["hashrate_24h"]
    rig_1 = herominers_API_keys["workers"][1]["name"]
    rig_2 = herominers_API_keys["workers"][0]["name"]
    rig_1_current_hashrate = herominers_API_keys["workers"][1]["hashrate"]
    rig_2_current_hashrate = herominers_API_keys["workers"][0]["hashrate"]

    #ERGO Payment data, rounded to 2 decimals
    total_paid_ergo = int(herominers_API_keys["stats"]["paid"]) / 1000000000
    total_paid_ergo = round(total_paid_ergo, 2)
    pending_balance_ergo = int(herominers_API_keys["stats"]["balance"]) / 1000000000
    pending_balance_ergo = round(pending_balance_ergo, 2)




    #Function for changing large numbers to Kilos, Megas etc.
    def hashrate_format(number):
        units = ['', ' KH', ' MH', ' GH', ' TH', ' PH']
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k**magnitude, units[magnitude])

    #Printing out the data in correct form


    with open("/var/www/html/herominers_output.txt", "w") as file:

        #Hashrate data
        file.write("Hashrates:\n")
        file.write(f"\n{rig_1}: {hashrate_format(rig_1_current_hashrate)}\n")
        file.write(f"{rig_2}: {hashrate_format(rig_2_current_hashrate)}\n")
        file.write("Total:\n")
        file.write(f"Current: {hashrate_format(current_hashrate)}\n")
        file.write(f"Average 24h: {hashrate_format(avg_24h_hashrate)}\n")

        #ERGO Payment data
        file.write("\nERGO:\n")
        file.write(f"\nTotal Paid: {total_paid_ergo} ERG\n")
        file.write(f"Pending Balance: {pending_balance_ergo} ERG\n")

if __name__ == '__main__':
    herominers_requests()
